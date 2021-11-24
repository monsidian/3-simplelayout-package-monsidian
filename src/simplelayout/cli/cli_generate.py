import sys
import argparse


def get_options():
    parser = argparse.ArgumentParser()
    # TODO: 按 1-simplelayout-CLI 要求添加相应参数
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs='+')
    parser.add_argument("--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    options = parser.parse_args()
    if options.board_grid % options.unit_grid:
        sys.exit("cannot divide exactly.")
    if len(options.positions) != options.unit_n:
        sys.exit("error: numbers of unit.")
    for position in options.positions:
        if position < 1 or \
                position > (options.board_grid / options.unit_grid) ** 2:
            sys.exit("position is beyond boundary.")
    return options
