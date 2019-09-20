import argparse
import time
import brainflow


def main ():
    parser = argparse.ArgumentParser ()
    parser.add_argument ('--port', type = str, help  = 'port name, for synthetic board port_name doesnt matter, just pass smth', required = True)
    parser.add_argument ('--board', type = int, help  = 'board id, Ganglion: 1, Cyton: 0, Synthetic: -1', required = True)
    parser.add_argument ('--log', action = 'store_true')
    args = parser.parse_args ()

    if (args.log):
        brainflow.board_shim.BoardShim.enable_dev_board_logger ()
    else:
        brainflow.board_shim.BoardShim.disable_board_logger ()

    board = brainflow.board_shim.BoardShim (args.board, args.port)
    board.prepare_session ()
    
    # disable second channel, note emulator doesnt handle such commands, run with real board to validate
    # different board have different data formats
    if args.board in (brainflow.CYTON.board_id, brainflow.CYTON_DAISY.board_id, brainflow.SYNTHETIC.board_id, brainflow.NOVAXR.board_id):
        board.config_board ('x2100000X')
    elif args.board == brainflow.GANGLION.board_id:
        board.config_board ('2')
    else:
        print ('unexpected board id')

    board.start_stream ()
    time.sleep (10)
    data = board.get_board_data ()
    board.stop_stream ()
    board.release_session ()

    data_handler = brainflow.preprocess.DataHandler (args.board, numpy_data = data)
    filtered_data = data_handler.preprocess_data (order = 3, start = 1, stop = 50)


if __name__ == "__main__":
    main ()
