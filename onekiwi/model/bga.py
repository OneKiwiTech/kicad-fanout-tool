import pcbnew
import math

class BGA:
    def __init__(self, board, reference, track, via, alignment, direction, logger):
        self.logger = logger
        self.board = board
        self.reference = reference
        self.track = track
        self.via = via
        self.alignment = alignment
        self.direction = direction
        self.pitchx = 0
        self.pitchy = 0
        self.tracks = []

        self.logger.info(reference)
        self.radian_pad = 0.0
        self.footprint = self.board.FindFootprintByReference(reference)
        self.radian = self.footprint.GetOrientation().AsRadians()
        self.degrees = self.footprint.GetOrientation().AsDegrees()
        self.pads = self.footprint.Pads()
        self.x0 = self.footprint.GetPosition().x
        self.y0 = self.footprint.GetPosition().y
        self.init_data()
    
    def init_data(self):
        if self.degrees not in [0.0 , 90.0, 180.0, -90.0]:
            degrees = self.degrees + 45.0
            self.footprint.SetOrientationDegrees(degrees)
            self.radian_pad = self.footprint.GetOrientation().AsRadians()
            self.footprint.SetOrientationDegrees(0)
        pos_x = []
        pos_y = []

        minx = self.pads[0].GetPosition().x
        maxx = self.pads[0].GetPosition().x
        miny = self.pads[0].GetPosition().y
        maxy = self.pads[0].GetPosition().y

        pos_x.append([self.pads[0].GetPosition()])
        pos_y.append([self.pads[0].GetPosition()])
        
        for pad in self.pads:
            pos = pad.GetPosition()
            if minx > pos.x:
                minx = pos.x
            if maxx < pos.x:
                maxx = pos.x
            if miny > pos.y:
                miny = pos.y
            if maxy < pos.y:
                maxy = pos.y
            checkx = True
            for arr in pos_x:
                if arr[0].y == pos.y and pos not in arr:
                    checkx = False
                    arr.append(pos)
            if checkx == True:
                pos_x.append([pos])
            
            checky = True
            for arr in pos_y:
                if arr[0].x == pos.x and pos not in arr:
                    checky = False
                    arr.append(pos)
            if checky == True:
                pos_y.append([pos])
            
        for arrs in pos_x:
            arrs.sort(key=lambda x:x.x)
        for arrs in pos_y:
            arrs.sort(key=lambda x:x.y)
        
        self.pitchx = pos_x[0][1].x - pos_x[0][0].x
        for arrs in pos_x:
            for i in range(len(arrs)):
                if i > 0:
                    pitch = arrs[i].x - arrs[i-1].x
                    if pitch > 0 and pitch < self.pitchx:
                        self.pitchx = pitch
        
        self.pitchy = pos_y[0][1].y - pos_y[0][0].y
        for arrs in pos_y:
            for i in range(len(arrs)):
                if i > 0:
                    pitch = arrs[i].y - arrs[i-1].y
                    if pitch > 0 and pitch < self.pitchy:
                        self.pitchy = pitch
        self.logger.info('pitch x: %d' %self.pitchx)
        self.logger.info('pitch y: %d' %self.pitchy)
        self.footprint.SetOrientationDegrees(self.degrees)
        
    def fanout(self):
        if self.alignment == 'Quadrant':
            if self.degrees in [0.0 , 90.0, 180.0, -90.0]:
                self.quadrant_0_90_180()
            elif self.degrees in [45.0 , 135.0, -135.0, -45.0]:
                self.quadrant_45_135()
            else:
                self.quadrant_other_angle()
        elif self.alignment == 'Diagonal':
            if self.degrees in [0.0 , 90.0, 180.0, -90.0]:
                self.diagonal_0_90_180()
            elif self.degrees in [45.0 , 135.0, -135.0, -45.0]:
                self.diagonal_45_135()
            else:
                self.diagonal_other_angle()
        elif self.alignment == 'X-pattern':
            if self.degrees in [0.0 , 90.0, 180.0, -90.0]:
                self.xpattern_0_90_180()
            elif self.degrees in [45.0 , 135.0, -135.0, -45.0]:
                self.xpattern_45_135()
            else:
                self.xpattern_other_angle()
            
        pcbnew.Refresh()

    # quadrant
    def quadrant_0_90_180(self):
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            if pos.y > self.y0:
                if pos.x > self.x0:
                    # bottom-right 225
                    x = pos.x + self.pitchx/2
                    y = pos.y + self.pitchy/2
                else:
                    # bottom-left 135
                    x = pos.x - self.pitchx/2
                    y = pos.y + self.pitchy/2
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)
            else:
                if pos.x > self.x0:
                    # top-right 315
                    x = pos.x + self.pitchx/2
                    y = pos.y - self.pitchy/2
                else:
                    # top-left 45
                    x = pos.x - self.pitchx/2
                    y = pos.y - self.pitchy/2
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)
    
    def quadrant_45_135(self):
        bx = self.y0 + self.x0
        by = self.y0 - self.x0
        pitch = math.sqrt(self.pitchx*self.pitchx + self.pitchy*self.pitchy)/2
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            y1 = bx - pos.x
            y2 = by + pos.x
            if pos.y > y1:
                if pos.y > y2:
                    # bottom
                    x = pos.x
                    y = pos.y + pitch
                else:
                    # left
                    x = pos.x + pitch
                    y = pos.y
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)
            else:
                if pos.y > y2:
                    # right
                    x = pos.x - pitch
                    y = pos.y
                else:
                    # top
                    x = pos.x
                    y = pos.y - pitch
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)

    def quadrant_other_angle(self):
        anphalx = (-1)*math.tan(self.radian)
        anphaly = 1/math.tan(self.radian)
        bx0 = self.y0 - anphalx*self.x0
        by0 = self.y0 - anphaly*self.x0
        
        pax = -1*math.tan(self.radian_pad)
        pay = 1/math.tan(self.radian_pad)
        pitch = math.sqrt(self.pitchx*self.pitchx + self.pitchy*self.pitchy)/2
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            y1 = anphalx*pos.x + bx0
            y2 = anphaly*pos.x + by0
            pbx = pos.y - pax*pos.x
            pby = pos.y - pay*pos.x

            # d^2 = (x - x0)^2 + (y - y0)^2
            #     = (x - x0)^2 + (a.x + b - y0)^2
            #     = #x^2 - #2x.x0 + #x0^2 + #a^2.x^2 + #a.b.x - #a.y0.x + #a.b.x + #b^2 - #b.y0 - #a.y0.x - b.y0 + y0^2
            # = (1 + a.a)x.x = (-2.x0 + 2.a.b - 2.a.y0)x + (x0.x0 + b.b - 2.b.y0 + y0.y0) - d.d
            ax = pax*pax + 1
            bx = 2*pax*pbx - 2*pos.x - 2*pax*pos.y
            cx = pos.x*pos.x + pbx*pbx + pos.y*pos.y - 2*pbx*pos.y - pitch*pitch

            ay = pay*pay + 1
            by = 2*pay*pby - 2*pos.x - 2*pay*pos.y
            cy = pos.x*pos.x + pby*pby + pos.y*pos.y - 2*pby*pos.y - pitch*pitch

            deltax = bx*bx - 4*ax*cx
            deltay = by*by - 4*ay*cy
            if deltax > 0:
                x1 = (-(bx) + math.sqrt(deltax))/(2*ax)
                x2 = (-(bx) - math.sqrt(deltax))/(2*ax)
            if deltay > 0:
                x3 = (-(by) + math.sqrt(deltay))/(2*ay)
                x4 = (-(by) - math.sqrt(deltay))/(2*ay)
            degrees_0to45 = self.degrees > 0 and self.degrees < 45
            degrees_45to90 = self.degrees > 45 and self.degrees < 90
            degrees_90to135 = self.degrees > 90 and self.degrees < 135
            degrees_135to180 =self.degrees > 135 and self.degrees < 180
            degrees_0to90 = self.degrees > 0 and self.degrees < 90
            degrees_90to180 =self.degrees > 90 and self.degrees < 180

            degrees_n45to0 = self.degrees > -45 and self.degrees < 0
            degrees_n90to45 = self.degrees > -90 and self.degrees < -45
            degrees_n135to90 = self.degrees > -135 and self.degrees < -90
            degrees_n180to135 =self.degrees > -180 and self.degrees < -135
            degrees_n180to90 =self.degrees > -180 and self.degrees < -90
            degrees_n90to0 = self.degrees > -90 and self.degrees < 0
            if pos.y > y1:
                x = 0
                y = 0
                if pos.y > y2:
                    # bottom-left
                    if degrees_0to45 or degrees_n180to135:
                        x = x2
                        y = pax*x + pbx
                    elif degrees_45to90 or degrees_n135to90:
                        x = x1
                        y = pax*x + pbx
                    elif degrees_90to135 or degrees_n90to45:
                        x = x4
                        y = pay*x + pby
                    elif degrees_135to180 or degrees_n45to0:
                        x = x3
                        y = pay*x + pby

                else:
                    # bottom-right
                    if degrees_0to90 or degrees_n180to90:
                        x = x3
                        y = pay*x + pby
                    elif degrees_90to180 or degrees_n90to0:
                        x = x2
                        y = pax*x + pbx
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)
            else:
                x = 0
                y = 0
                if pos.y > y2:
                    # top-left
                    if degrees_0to90 or degrees_n180to90:
                        x = x4
                        y = pay*x + pby
                    elif degrees_90to180 or degrees_n90to0:
                        x = x1
                        y = pax*x + pbx
                else:
                    # bottom-right
                    if degrees_0to45 or degrees_n180to135:
                        x = x1
                        y = pax*x + pbx
                    elif degrees_45to90 or degrees_n135to90:
                        x = x2
                        y = pax*x + pbx
                    elif degrees_90to135 or degrees_n90to45:
                        x = x3
                        y = pay*x + pby
                    elif degrees_135to180 or degrees_n45to0:
                        x = x4
                        y = pay*x + pby
                end = pcbnew.wxPoint(x, y)
                self.add_track(net, pos, end)
                self.add_via(net, end)

    # diagonal
    def diagonal_0_90_180(self):
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            x = 0
            y = 0
            if self.direction =='TopLeft':
                x = pos.x - self.pitchx/2
                y = pos.y - self.pitchy/2
            if self.direction =='TopRight':
                x = pos.x + self.pitchx/2
                y = pos.y - self.pitchy/2
            if self.direction =='BottomLeft':
                x = pos.x - self.pitchx/2
                y = pos.y + self.pitchy/2
            if self.direction =='BottomRight':
                x = pos.x + self.pitchx/2
                y = pos.y + self.pitchy/2
            end = pcbnew.wxPoint(x, y)
            self.add_track(net, pos, end)
            self.add_via(net, end)

    def diagonal_45_135(self):
        pitch = math.sqrt(self.pitchx*self.pitchx + self.pitchy*self.pitchy)/2
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            x = pos.x
            y = pos.y
            if self.direction =='TopLeft':
                x = pos.x - pitch
                y = pos.y
            if self.direction =='TopRight':
                x = pos.x + pitch
                y = pos.y
            if self.direction =='BottomLeft':
                x = pos.x
                y = pos.y + pitch
            if self.direction =='BottomRight':
                x = pos.x
                y = pos.y - pitch
            end = pcbnew.wxPoint(x, y)
            self.add_track(net, pos, end)
            self.add_via(net, end)

    def diagonal_other_angle(self):
        pax = -1*math.tan(self.radian_pad)
        pay = 1/math.tan(self.radian_pad)
        pitch = math.sqrt(self.pitchx*self.pitchx + self.pitchy*self.pitchy)/2
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            pbx = pos.y - pax*pos.x
            pby = pos.y - pay*pos.x

            # d^2 = (x - x0)^2 + (y - y0)^2
            #     = (x - x0)^2 + (a.x + b - y0)^2
            #     = #x^2 - #2x.x0 + #x0^2 + #a^2.x^2 + #a.b.x - #a.y0.x + #a.b.x + #b^2 - #b.y0 - #a.y0.x - b.y0 + y0^2
            # = (1 + a.a)x.x = (-2.x0 + 2.a.b - 2.a.y0)x + (x0.x0 + b.b - 2.b.y0 + y0.y0) - d.d
            ax = pax*pax + 1
            bx = 2*pax*pbx - 2*pos.x - 2*pax*pos.y
            cx = pos.x*pos.x + pbx*pbx + pos.y*pos.y - 2*pbx*pos.y - pitch*pitch

            ay = pay*pay + 1
            by = 2*pay*pby - 2*pos.x - 2*pay*pos.y
            cy = pos.x*pos.x + pby*pby + pos.y*pos.y - 2*pby*pos.y - pitch*pitch

            deltax = bx*bx - 4*ax*cx
            deltay = by*by - 4*ay*cy
            if deltax > 0:
                x1 = (-(bx) + math.sqrt(deltax))/(2*ax)
                x2 = (-(bx) - math.sqrt(deltax))/(2*ax)
            if deltay > 0:
                x3 = (-(by) + math.sqrt(deltay))/(2*ay)
                x4 = (-(by) - math.sqrt(deltay))/(2*ay)
            x = pos.x
            y = pos.y
            if self.direction =='TopLeft':
                x = x4
                y = pay*x + pby
            if self.direction =='TopRight':
                x = x2
                y = pax*x + pbx
            if self.direction =='BottomLeft':
                x = x1
                y = pax*x + pbx
            if self.direction =='BottomRight':
                x = x3
                y = pay*x + pby
            end = pcbnew.wxPoint(x, y)
            self.add_track(net, pos, end)
            self.add_via(net, end)

    #X-pattern
    def xpattern_0_90_180(self):
        bx = self.y0 + self.x0
        by = self.y0 - self.x0
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            y1 = bx - pos.x
            y2 = by + pos.x
            x = 0
            y = 0
            if pos.y > y1:
                if pos.y > y2:
                    #bottom
                    if self.direction =='Counterclock':
                        x = pos.x - self.pitchx/2
                        y = pos.y + self.pitchy/2
                    if self.direction =='Counterclockwise':
                        x = pos.x + self.pitchx/2
                        y = pos.y + self.pitchy/2
                else:
                    #right
                    if self.direction =='Counterclock':
                        x = pos.x + self.pitchx/2
                        y = pos.y + self.pitchy/2
                    if self.direction =='Counterclockwise':
                        x = pos.x + self.pitchx/2
                        y = pos.y - self.pitchy/2
            else:
                if pos.y > y2:
                    #left
                    if self.direction =='Counterclock':
                        x = pos.x - self.pitchx/2
                        y = pos.y - self.pitchy/2
                    if self.direction =='Counterclockwise':
                        x = pos.x - self.pitchx/2
                        y = pos.y + self.pitchy/2
                else:
                    #top
                    if self.direction =='Counterclock':
                        x = pos.x + self.pitchx/2
                        y = pos.y - self.pitchy/2
                    if self.direction =='Counterclockwise':
                        x = pos.x - self.pitchx/2
                        y = pos.y - self.pitchy/2
            end = pcbnew.wxPoint(x, y)
            self.add_track(net, pos, end)
            self.add_via(net, end)
    
    def xpattern_45_135(self):
        pitch = math.sqrt(self.pitchx*self.pitchx + self.pitchy*self.pitchy)/2
        for pad in self.pads:
            pos = pad.GetPosition()
            net = pad.GetNetCode()
            x = 0
            y = 0
            if pos.y > self.y0:
                if pos.x > self.x0:
                    #bottom-right
                    if self.direction =='Counterclock':
                        x = pos.x
                        y = pos.y + pitch
                    if self.direction =='Counterclockwise':
                        x = pos.x + pitch
                        y = pos.y
                else:
                    #bottom-left
                    if self.direction =='Counterclock':
                        x = pos.x - pitch
                        y = pos.y
                    if self.direction =='Counterclockwise':
                        x = pos.x
                        y = pos.y + pitch
            else:
                if pos.x > self.x0:
                    #bottom-right
                    if self.direction =='Counterclock':
                        x = pos.x + pitch
                        y = pos.y
                    if self.direction =='Counterclockwise':
                        x = pos.x
                        y = pos.y - pitch
                else:
                    #bottom-left
                    if self.direction =='Counterclock':
                        x = pos.x
                        y = pos.y - pitch
                    if self.direction =='Counterclockwise':
                        x = pos.x - pitch
                        y = pos.y
                    
            end = pcbnew.wxPoint(x, y)
            self.add_track(net, pos, end)
            self.add_via(net, end)

    def xpattern_other_angle(self):
        # TODO, not implemented
        self.logger.error('X pattern for arbitrary angles not implemented yet, use 45, 90, 135, 180 instead')

    def add_track(self, net, start, end):
        track = pcbnew.PCB_TRACK(self.board)
        track.SetStart(start)
        track.SetEnd(pcbnew.VECTOR2I(end))
        track.SetWidth(self.track)
        track.SetLayer(pcbnew.F_Cu)
        track.SetNetCode(net)
        self.board.Add(track)
        self.tracks.append(track)
    
    def add_via(self, net, pos):
        via = pcbnew.PCB_VIA(self.board)
        via.SetViaType(pcbnew.VIATYPE_THROUGH)
        via.SetPosition(pcbnew.VECTOR2I(pos))
        via.SetWidth(int(self.via.m_Diameter))
        via.SetDrill(self.via.m_Drill)
        via.SetNetCode(net)
        self.board.Add(via)
        self.tracks.append(via)

    def remove_track_via(self):
        for item in self.tracks:
            self.board.Remove(item)
        self.tracks.clear()
        pcbnew.Refresh()
