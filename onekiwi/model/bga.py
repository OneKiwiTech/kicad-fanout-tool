import pcbnew
import math

class BGA:
    def __init__(self, board, reference, track, via, logger):
        self.logger = logger
        self.board = board
        self.reference = reference
        self.track = track
        self.via = via
        self.pitchx = 0
        self.pitchy = 0

        self.logger.info(reference)
        self.footprint = self.board.FindFootprintByReference(reference)
        self.radian = self.footprint.GetOrientationRadians()
        self.degrees = self.footprint.GetOrientationDegrees()
        self.pads = self.footprint.Pads()
        self.x0 = self.footprint.GetPosition().x
        self.y0 = self.footprint.GetPosition().y
        self.init_data()
    
    def init_data(self):
        if self.degrees not in [0.0 , 90.0, 180.0, -90.0]:
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
        """
        for ind, arrs in enumerate(pos_y):
            self.logger.info('%d. sort---------------------' %ind)
            for i, arr in enumerate(arrs):
                self.logger.info('%d. %s' %(i, str(arr)))
        """
        self.footprint.SetOrientationDegrees(self.degrees)

        if self.degrees in [0.0 , 90.0, 180.0, -90]:
            x = (minx + maxx)/2
            y = (miny + maxy)/2
            xstart = pcbnew.wxPoint(x, maxy)
            xend = pcbnew.wxPoint(x, miny)
            ystart = pcbnew.wxPoint(minx, y)
            yend = pcbnew.wxPoint(maxx, y)
            xtrack = pcbnew.PCB_TRACK(self.board)
            xtrack.SetStart(xstart)
            xtrack.SetEnd(xend)
            xtrack.SetWidth(self.track)
            xtrack.SetLayer(pcbnew.F_Cu)
            self.board.Add(xtrack)

            ytrack = pcbnew.PCB_TRACK(self.board)
            ytrack.SetStart(ystart)
            ytrack.SetEnd(yend)
            ytrack.SetWidth(self.track)
            ytrack.SetLayer(pcbnew.F_Cu)
            self.board.Add(ytrack)
        else:
            anphalx = (-1)*math.tan(self.radian)
            anphaly = 1/math.tan(self.radian)
            bx = self.y0 - anphalx*self.x0
            by = self.y0 - anphaly*self.x0

            # y = ax + b
            xyminx = anphalx*minx + bx
            xymaxx = anphalx*maxx + bx
            xstart = pcbnew.wxPoint(minx, xyminx)
            xend = pcbnew.wxPoint(maxx, xymaxx)

            yyminx = anphaly*minx + by
            yymaxx = anphaly*maxx + by
            ystart = pcbnew.wxPoint(minx, yyminx)
            yend = pcbnew.wxPoint(maxx, yymaxx)

            xtrack = pcbnew.PCB_TRACK(self.board)
            xtrack.SetStart(xstart)
            xtrack.SetEnd(xend)
            xtrack.SetWidth(self.track)
            xtrack.SetLayer(pcbnew.F_Cu)
            self.board.Add(xtrack)

            ytrack = pcbnew.PCB_TRACK(self.board)
            ytrack.SetStart(ystart)
            ytrack.SetEnd(yend)
            ytrack.SetWidth(self.track)
            ytrack.SetLayer(pcbnew.F_Cu)
            self.board.Add(ytrack)
        pcbnew.Refresh()
    
    def fanout(self):
        if self.degrees in [0.0 , 90.0, 180.0, -90.0]:
            for pad in self.pads:
                pos = pad.GetPosition()
                net = pad.GetNetCode()
                if pos.y > self.y0:
                    if pos.x > self.x0:
                        # II 225
                        x = pos.x + self.pitchx/2
                        y = pos.y + self.pitchy/2
                    else:
                        # III 135
                        x = pos.x - self.pitchx/2
                        y = pos.y + self.pitchy/2
                    end = pcbnew.wxPoint(x, y)
                    self.add_track(net, pos, end)
                    self.add_via(net, end)
                else:
                    if pos.x > self.x0:
                        # I 315
                        x = pos.x + self.pitchx/2
                        y = pos.y - self.pitchy/2
                    else:
                        # IV 45
                        x = pos.x - self.pitchx/2
                        y = pos.y - self.pitchy/2
                    end = pcbnew.wxPoint(x, y)
                    self.add_track(net, pos, end)
                    self.add_via(net, end)
        pcbnew.Refresh()
    
    def add_track(self, net, start, end):
        track = pcbnew.PCB_TRACK(self.board)
        track.SetStart(start)
        track.SetEnd(end)
        track.SetWidth(self.track)
        track.SetLayer(pcbnew.F_Cu)
        track.SetNetCode(net)
        self.board.Add(track)
    
    def add_via(self, net, pos):
        via = pcbnew.PCB_VIA(self.board)
        via.SetViaType(pcbnew.VIATYPE_THROUGH)
        via.SetPosition(pos)
        via.SetWidth(int(self.via.m_Diameter))
        via.SetDrill(self.via.m_Drill)
        via.SetNetCode(net)
        self.board.Add(via)
