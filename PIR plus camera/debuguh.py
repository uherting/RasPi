# special to Raspberry Pi
from gpiozero import PiBoardInfo

class debuguh_out:
    def show_info(self, debug):
        #
        # DUMMY START
        #

        if debug == 1:
            pi_model = 'M'  # PiBoardInfo.model
            pi_rev = 'R'  # PiBoardInfo.revision
            pi_pcbrev = 'PR'  # PiBoardInfo.pcb_revision
        else:
            pi_model = PiBoardInfo.model
            pi_rev = PiBoardInfo.revision
            pi_pcbrev = PiBoardInfo.pcb_revision

        print('PiBoardInfo')
        print('\tModel: ' + pi_model)
        print('\tRevision: ' + pi_rev)
        print('\tPCB-Rev.: ' + pi_pcbrev)

        #
        # DUMMY END
        #

