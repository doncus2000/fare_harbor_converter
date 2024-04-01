# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on apr 21st, 2023

@author: Donald R. Custer doncus2000@gmail.com 707-483-8831

AOW 
Copyright2023 AOW, Inc.  All rights reserved.
This work is licensed under the Gnome Public License.
As such code must be made available to open source
"""
import os
import inspect
import re


class fareHarborConverter:

    def __init__(self):
        pass

    def find_files(self, directory):
        """
        Find csv files in directory specified.
        :param directory: directory to search
        :return: files a list of paths to files
        """
        try:
            files = []
            if directory:
                for filename in os.listdir(directory):
                    f = os.path.join(directory, filename)
                    # checking if it is a file
                    if os.path.isfile(f):
                        if '.csv' in f:
                            files.append(f)
            print(f"Found Files: {files} \n")
            return files
        except Exception as ex:
            msg = inspect.stack()[0][3], str(ex)
            print(msg)

    def scrub_text(self, raw_line):
        """
        Remove useless data
        :param raw_line: line of text to scrub
        :return: processed line
        """
        try:
            line = None
            line = raw_line.replace('"','').replace(',,,','').replace('-','').strip()
            return line
        except Exception as ex:
            msg = inspect.stack()[0][3], str(ex)
            print(msg)

    def get_file_data(self, filename):
        """
        Process data from a csv file to gather tour data.
        param filename: the path to the file that contains data to be processed
        return: tours
        """
        try:
            guide_run = False
            tour = {}
            tours = []
            guides = []
            guide_arg = r"Guide\sis\s(\w*)\s(\w*)|Guide\sis\s(\w*)"
            tour_arg = r"(.*)\s*,\s*(\d+:*\d*[ap]m)\s*(\d+:*\d*[ap]m)"
            guest_arg = r"(.*)\s*,\s*\d+\s*[aA]dults|(.*)\s*,\s*\d+\s*[gG]uests|(.*)\s*,\s*\d+\s*[yY]outh"
            if filename:
                with open(filename, newline='') as csvfile:
                    for raw_line in csvfile:
                        line = self.scrub_text(raw_line)
                        guide = re.findall(guide_arg, line)
                        if guide:
                            if not guide_run:
                                guides.clear()
                            guide_run = True
                            guides.append("".join(guide[0]))
                            tour['guide'] = f'Guide is {" and ".join(guides)}'
                        tour_name = re.findall(tour_arg, line)
                        if tour_name:
                            tour['tour_name'] = tour_name[0][0]
                            if ':' in tour_name[0][1]:
                                tour['start_time'] = tour_name[0][1].replace('am', ' AM').replace('pm', ' PM')
                            else:
                                tour['start_time'] = tour_name[0][1].replace('am', ':00 AM').replace('pm', ':00 PM')
                            if ':' in tour_name[0][2]:
                                tour['end_time'] = tour_name[0][2].replace('am', ' AM').replace('pm', ' PM')
                            else:
                                tour['end_time'] = tour_name[0][2].replace('am', ':00 AM').replace('pm', ':00 PM')
                            if not tour.get('guide') or not guide_run:
                                tour['guide'] = 'Guide is Not Yet Scheduled'
                        guest = re.findall(guest_arg, line)
                        if guest:
                            guest_name = "".join(guest[0])
                            tours.append(f"{guest_name},{tour['tour_name']},{tour['start_time']},{tour['end_time']},"
                                         f"{tour['guide']}")
                            guide_run = False
            return tours
        except Exception as ex:
            msg = inspect.stack()[0][3], str(ex)
            print(msg)

    def print_data(self, tours, file):
        """
        Out put processed data to file and to screen.
        param tours:
        param file:
        return: nothing
        """
        try:
            dest = file.replace('input', 'output')
            print(f"------------------------------\n"
                  f"--Printing file {dest} -- \n")
            if os.path.exists(dest):
                print(f"Deleting old version and reprinting file {dest} \n")
                os.remove(dest)
            with open(dest, 'a') as filehandle:
                line_1 = "Guest,Tour,Start,End,Driver"
                filehandle.write(line_1 + '\n')
                print(line_1)
                for tour in tours:
                    filehandle.write(tour + '\n')
                    print(tour)
        except Exception as ex:
            msg = inspect.stack()[0][3], str(ex)
            print(msg)

    def run(self):
        """
        Executes processing tour data from one csv and converts it into a formatted csv .
        param:
        return: nothing
        """
        try:
            files = self.find_files('input')
            for file in files:
                self.print_data(self.get_file_data(file), file)
        except Exception as ex:
            msg = inspect.stack()[0][3], str(ex)
            print(msg)


def main():
    test = fareHarborConverter()
    test.run()


if __name__ == '__main__':
    main()
