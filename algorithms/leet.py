#! /usr/bin/env python

# -*- coding: utf-8 -*-

import json
import os
import sys

import requests


def get_problems():
    with open('problem.json', 'r') as f:
        return json.load(f)


def update_problems():
    """
    request leetcode api to get all problem and save into a json file
    :return:
    """
    with open('problem.json', 'w') as f:
        problems = {}
        resp = requests.get('https://leetcode.com/api/problems/algorithms/').json()
        for problem in resp.get('stat_status_pairs'):
            problem_id = problem['stat']['question_id']
            problem_title = problem['stat']['question__title_slug']
            problems[problem_id] = problem_title

        print('fetch {number} problems from leetcode'.format(number=len(problems)))
        f.write(json.dumps(problems, indent=2))


def rename_problems(category):
    """
    rename all solution code in a category, new name come from leetcode api
    :param category:
    :return:
    """
    problems = get_problems()
    dir = "./%s/" % category
    for filename in os.listdir(dir):
        num = filename[:filename.index('.')]
        print problems[num]
        print filename
        os.rename(dir + filename, dir + num + '.' + problems[num] + '.py')


def solve_problem(number, category):
    """
    render a code template to solve problem
    :param category:
    :param number: problem_id
    :return:
    """
    problems = get_problems()

    filepath = '{category}'.format(category=category)
    filename = '{category}/{number}.{title}.py'.format(category=category, number=number, title=problems[number])
    if not os.path.exists(filepath):
        os.mkdir(filepath)
        print '{filepath} is a new category'.format(filepath=filepath)

    if os.path.exists(filename):
        print '{filename} is already exists'.format(filename=filename)
    else:
        with open(filename, 'w') as f:
            code_template = """#! coding=utf8\n# ideas:\n# \n# gains:\n# \n\n\n"""
            f.write(code_template)
        print '{filename} was ready'.format(filename=filename)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        op = sys.argv[1]
        if op == 'update':
            update_problems()
        if op == 'solve':
            solve_problem(*sys.argv[2:])
        if op == 'rename':
            rename_problems(sys.argv[2])
