#Nome e data

def valid_date_type(arg_date_str):
    """custom argparse *date* type for user dates values given from the command line"""
    try:
        return datetime.datetime.strptime(arg_date_str, "%Y-%m-%d")
    except ValueError:
        msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(arg_date_str)
        raise argparse.ArgumentTypeError(msg)
        
def valid_datetime_type(arg_datetime_str):
    """custom argparse type for user datetime values given from the command line"""
    try:
        return datetime.datetime.strptime(arg_datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Given Datetime ({0}) not valid! Expected format, 'YYYY-MM-DD HH:mm'!".format(arg_datetime_str)
        raise argparse.ArgumentTypeError(msg)        
        
        
if __name__ == '__main__':
    import argparse
    parser = argparse.parser(description='Example of custom type usage')
    parser.add_argument('-s', '--start-datetime',
                        dest='start_datetime',
                        type=valid_datetime_type,
                        default=None,
                        required=True,
                        help='start datetime in format "YYYY-MM-DD HH:mm"')
    args = parser.parse_args()
    start_datetime_object = args.start_datetime
print(start_datetime_object)
