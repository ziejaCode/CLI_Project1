import sys
import argparse
from PySide2 import QtWidgets

shots_info = {
    "sh001": {"status": "Completed", "assign_to": "Rajiv Sharma"},
    "sh002": {"status": "InProgress", "assign_to": "Sapna Sharma"},
    "sh003": {"status": "New", "assign_to": "Aayaan Sharma"}
}


def display_info(shot_id, query_key):
    app = QtWidgets.QApplication()
    shot = shots_info.get(shot_id, None)
    if shot:
        if query_key:
            info = shots_info[shot_id][query_key]
            data = "{} {} is {}".format(shot_id, query_key, info)
        else:
            data = "{} {} ".format(shot_id, shots_info[shot_id])
    else:
        data = "{} is not exist".format(shot_id)
    QtWidgets.QMessageBox.information(None, 'Shots Info Tool', data)

#  display_info('sh003', 'status')

if __name__ == '__main__':
    #arg = sys.argv
    #print(arg)
    #display_info(arg[1], arg[2])
    
    parser = argparse.ArgumentParser(prog='Shot Info',
                                    usage='''
                                    Usage:
                                    Pass shots data in json format
                                    and this will rerun the value from the query key.
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will display shots information
                                    -----------------------------------------------
                                    ''',
                                    epilog="Copyrights @ Rajiv Sharma (www.hqvfx.com)",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )

    parser.add_argument("shot", type=str, help="Enter shot id. for example: sh001", metavar="SHOT LABEL ID")
    parser.add_argument("--key", "-k", type=str,
                        help="Optional: Enter query key for search information. for example: status", default='status',
                        required=False)
    arg = parser.parse_args()
    display_info(arg.shot, arg.key)
