from aas_displayer.aas_file import ASSFile

import argparse
import codecs
import sched
from kitchen.text.converters import getwriter
import time

# UTF8 and python 2 are not so friendly to each other, so we need to help them cross their problems:
# Taken from: https://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script
import sys

from aas_displayer.utils.relative_time import RelativeTime

reload(sys)
sys.setdefaultencoding("utf-8")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--file", dest="file_path", required=True, help="The path to the ASS file that you want to display.")
    return parser.parse_args()


def show_event(event):
    if event.should_display():
        event.display()
    sys.stdout.flush()


def main():
    args = parse_args()

    # Another hack for UTF8 support:
    # Taken from: https://pythonhosted.org/kitchen/unicode-frustrations.html
    utf8_writer = getwriter('utf8')
    sys.stdout = utf8_writer(sys.stdout)
    with codecs.open(args.file_path, encoding='utf-8') as f:
        text = f.read()

    ass = ASSFile(text)
    relative_time = RelativeTime()
    scheduler = sched.scheduler(time.time, time.sleep)
    for event in ass.events:
        start_time = event.start.to_seconds()
        scheduler.enter(start_time, time.time(), show_event, [event])
    relative_time.start()
    scheduler.run()


if __name__ == '__main__':
    main()