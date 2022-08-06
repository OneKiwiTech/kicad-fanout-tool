
class BGA:
    def __init__(self, board, reference, track, via, logger):
        self.logger = logger
        self.board = board
        self.reference = reference
        self.track = track
        self.via = via

        self.logger.info(reference)
        self.footprint = self.board.FindFootprintByReference(reference)
        self.angle = self.footprint.GetOrientationDegrees()
        self.pads = self.footprint.Pads()
        self.x0 = self.footprint.GetPosition().x
        self.y0 = self.footprint.GetPosition().y
        self.logger.info('aaaaaaaaaaaaaaaaaa')
        self.init_data()
    
    def init_data(self):
        if self.angle not in [0.0 , 90.0, 180.0, -90.0]:
            self.footprint.SetOrientationDegrees(0)
            self.logger.info('b3')
        arr_xy = []
        #name_xy = []
        
        pitch_x = 0
        pitch_y = 0
        minx = self.pads[0].GetPosition().x
        maxx = self.pads[0].GetPosition().x
        miny = self.pads[0].GetPosition().y
        maxy = self.pads[0].GetPosition().y
        temps = []
        #name_temp = []
        #name_temp.append(self.pads[0].GetPadName())
        #name_xy.append(name_temp)
        self.logger.info('b1')
        temps.append(self.pads[0].GetPosition())
        arr_xy.append(temps)
        self.logger.info('b2')
        a = arr_xy[0]
        self.logger.info(arr_xy)
        self.logger.info(a)
        self.logger.info(a[0])
        self.logger.info(a[0].x)
        
        for ind, pad in enumerate(self.pads, 1):
            pos = pad.GetPosition()
            if minx > pos.x:
                minx = pos.x
            if maxx < pos.x:
                maxx = pos.x
            if miny > pos.y:
                miny = pos.y
            if maxy < pos.y:
                maxy = pos.y
            
            for arrx in arr_xy:
                self.logger.info('b4')
                self.logger.info('%d - %d' %(arrx[0].y, pos.y))
                if arrx[0].y == pos.y:
                    arrx.append(pos)
                    self.logger.info('b5')
                    """
                else:
                    self.logger.info('b6')
                    temp = []
                    temp.append(pos)
                    arr_xy.append(temp)
                    self.logger.info('b7')
            """
        self.logger.info('bn')
        for arr in arr_xy:
            self.logger.info('---------------------')
            self.logger.info('%s' %str(arr))
        self.footprint.SetOrientationDegrees(self.angle)
