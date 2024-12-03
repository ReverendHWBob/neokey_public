# module for import

class macroM:

    def __init__(self):
        '''
        Give your macrolist a meaningful name
        Put your perfered key macro in the first tuple in the list macros, 
        put your perfered touch macro in the second tuple
        '''
        self.rawMac = self.createMacro()
        self.keyMac = self.rawMac['macros'][0]
        self.touchMac = self.rawMac['macros'][1]

    def createMacro(self):
        """
        macros dictionary. includes name and a list of macros
        macros: [ ( hex-key-Color, string to send ), ] # it's a list of tuples folks
        example:  ( 0x00FF00, "the key macro"
        Common errors, you ALWAYS need , to seperate the 2 macros.
        You can include more , but it uses memory and we only use the first 2
        """
		### color 0xFF0000 = Red
		### Color 0x00FF00 = Green
		### Color 0x0000FF = Blue
		### Color 0x313131 = kind of a dull gray		
        ################## Change this #####################################
        app = {
            'name': "some descriptive Name",
            'macros': [
                    ( 0xFF00FF, "Key Pressed" ),
                    ( 0x00FF00, "Touch Pressed" ),
            ],
        }
        return app
        ################# change nothing else #############################

    def getKeyMac(self):
            return self.keyMac

    def getTouchMac(self):
            return self.touchMac





