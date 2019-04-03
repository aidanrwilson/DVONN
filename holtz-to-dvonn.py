#!/usr/bin/python3

import coloredlogs
import logging
import os
import shutil
import sys

coloredlogs.install(fmt='%(levelname)s %(asctime)s,%(msecs)03d %(name)s[%(process)d] %(message)s',
                    date_fmt='%H:%M:%S')

CPP_EXTENSIONS       = ('.c', '.cc', '.cpp', '.cxx', '.h', '.hh', '.hpp', '.hxx')
BLOKS_STR            = 'BLOKS'
DVONN_STR            = 'DVONN'
RELAX_STR            = 'RELAX'
ZERTZ_STR            = 'ZERTZ'
DVONN_VERSION_STR    = 'VERSION_DVONN'
BLOKS_DEFINED_STR    = 'defined(VERSION_BLOKS)'
DVONN_DEFINED_STR    = 'defined(VERSION_DVONN)'
RELAX_DEFINED_STR    = 'defined(VERSION_RELAX)'
ZERTZ_DEFINED_STR    = 'defined(VERSION_ZERTZ)'
IF_STR               = '#if'
ELIF_STR             = '#elif'
ENDIF_STR            = '#endif'

def non_dvonn_statement_in(line_i):
    return (BLOKS_STR in line_i) or (RELAX_STR in line_i) or (ZERTZ_STR in line_i)

def non_dvonn_defined_statement_in(line_i):
    return (BLOKS_DEFINED_STR in line_i) or (RELAX_DEFINED_STR in line_i) or (ZERTZ_DEFINED_STR in line_i)

def dvonn_version_statement_in(line_i):
    return (DVONN_VERSION_STR in line_i)

def line_clean_of_non_dvonn_games(line_i):
    return (not non_dvonn_statement_in(line_i)) and (not non_dvonn_statement_in(line_i.upper())) and (DVONN_VERSION_STR not in line_i)

def replace_holtz(line_i):
    temp = line_i.replace('holtz', 'dvonn')
    temp = temp.replace('Holtz', 'Dvonn')
    temp = temp.replace('HOLTZ', 'DVONN')
    return temp

def find_non_dvonn_function(lines, start_idx):
    i = start_idx
    while i < len(lines):
        open_paren  = lines[i].find('(')
        close_paren = lines[i].find(')')
        if (open_paren < close_paren) and not non_dvonn_statement_in(lines[i].upper()):
             # = (lines[i].find(')') < lines[i].find(';'))
            assert('{' in lines[i] or '{' in lines[i+1])
            function_declaration = i

def dedent_cleaned_directive(line_i):
    if not line_i.startswith('#'):
        return line_i
        # raise ValueError('Cleaned line to be dedented must be a preprocessor directive, beginning with "#"')
    start_idx = len(line_i) - (len(line_i) % 2) - 2
    for num_directive_spaces in range(start_idx, 0, 2):
        directive_indent = '#' + (' '*num_directive_spaces)
        if line_i.startswith(directive_indent):
            return '#' + line_i[num_directive_spaces + 1:]
    return '#' + line_i[1:]

def clean_file(filepath, new_filepath):
    lines    = tuple(open(filepath, 'r'))
    newlines = []
    num_lines_removed  = 0
    num_lines_dedented = 0
    i = 0
    while (i < len(lines)):
        ###############################################
        ##### HANDLE FUNCTIONS OF NON-DVONN GAMES #####
        ###############################################

        if '()'

        #############################################################
        ##### HANDLE PREPROCESSOR DIRECTIVES OF NON-DVONN GAMES #####
        #############################################################

        if (IF_STR in lines[i]) and non_dvonn_defined_statement_in(lines[i]):
            i += 1
            num_lines_removed += 1
            while (ENDIF_STR not in lines[i]) and (ELIF_STR not in lines[i]):
                i += 1
                num_lines_removed += 1
            continue

        if ((IF_STR in lines[i]) or (ELIF_STR in lines[i])) and (DVONN_DEFINED_STR in lines[i]):
            i += 1
            num_lines_removed += 1
            if non_dvonn_statement_in(lines[i]):
                i += 1
                num_lines_removed += 1
                continue
            while (ENDIF_STR not in lines[i]) and (ELIF_STR not in lines[i]):
                if (DVONN_VERSION_STR not in lines[i]):
                    num_lines_dedented += 1
                    newlines.append(dedent_cleaned_directive(lines[i]))
                else:
                    num_lines_removed += 1
                i += 1
            continue

        ##################################################################
        ##### HANDLE LAST MENTIONS OF NON-DVONN GAMES, REPLACE HOLTZ #####
        ##################################################################

        if line_clean_of_non_dvonn_games(lines[i]):
            temp = replace_holtz(lines[i])
            newlines.append(temp)
        else:
            num_lines_removed += 1

        i += 1

    logging.info("During cleaning process, removed %s lines and dedented %s preprocessor directives from file %s"
                 % (num_lines_removed, num_lines_dedented, filepath))
    lines = tuple(newlines)
    with open(new_filepath, 'w+') as newfile:
        logging.info("Writing version of file %s cleaned of all non-DVONN focused code to file %s"
                     % (filepath, new_filepath))
        for line_i in lines:
            newfile.write(line_i)


if __name__=='__main__':
    basepath = None
    clean_directory = None
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            basepath = arg
        if arg in ['-d', '--clean-dir', '--clean-directory']:
            clean_directory = True
        elif arg in ['-f', '--clean-filecopies']:
            clean_directory = False

    assert(basepath is not None)
    assert(clean_directory is not None)

    for root, dirs, files in os.walk(basepath, topdown=False):
        if root.endswith('clean'):
            shutil.rmtree(root)
            continue
        for file_i in files:
            if file_i.endswith('.clean') or file_i.endswith('.cleaned'):
                os.remove(os.path.join(root, file_i))

    if clean_directory:
        cleanpath = os.path.join(basepath, 'clean')
        if not os.path.isdir(cleanpath):
            os.mkdir(cleanpath)
        for root, dirs, files in os.walk(basepath):
            newroot = root.replace(basepath, cleanpath)
            if not os.path.isdir(newroot):
                os.mkdir(newroot)
            for filename in files:
                if not filename.endswith(CPP_EXTENSIONS):
                    shutil.copyfile(os.path.join(root, filename), os.path.join(newroot, filename))
                    continue
                clean_file(os.path.join(root, filename), os.path.join(newroot, filename))
    else:
        for root, dirs, files in os.walk(basepath):
            for filename in files:
                if not filename.endswith(CPP_EXTENSIONS):
                    continue
                clean_file(os.path.join(root, filename), os.path.join(root, filename + '.clean'))
