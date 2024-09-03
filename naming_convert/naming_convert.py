# -*- coding: utf-8 -*-

import re

split_case_regex = re.compile(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|[-_.\s]')

def to_pascal_case(s: str) -> str:
    """
    Convert string to PascalCase
    """
    return ''.join([w.capitalize() for w in split_case_regex.split(s)])


def to_camel_case(s: str) -> str:
    """
    Convert string to camelCase
    """
    head, *tail = split_case_regex.split(s)
    return head.casefold() + ''.join(w.capitalize() for w in tail)


def to_snake_case(s: str) -> str:
    """
    Convert string to snake_case
    """
    return '_'.join(w.casefold() for w in split_case_regex.split(s))


def to_screaming_snake_case(s: str) -> str:
    """
    Convert string to SCREAMING_SNAKE_CASE
    """
    return '_'.join(w.upper() for w in split_case_regex.split(s))


def to_kebab_case(s: str) -> str:
    """
    Convert string to kebab-case
    """
    return '-'.join(w.casefold() for w in split_case_regex.split(s))

def to_train_case(s: str) -> str:
    """
    Convert string to Train-Case
    """
    return '-'.join(w.capitalize() for w in split_case_regex.split(s))

def to_screaming_kebab_case(s: str) -> str:
    """
    Convert string to SCREAMING-KEBAB-CASE
    """
    return '-'.join(w.upper() for w in split_case_regex.split(s))


def to_dot_case(s: str) -> str:
    """
    Convert string to dot.case
    """
    return '.'.join(w.casefold() for w in split_case_regex.split(s))


def to_screaming_dot_case(s: str) -> str:
    """
    Convert string to SCREAMING.DOT.CASE
    """
    return '.'.join(w.upper() for w in split_case_regex.split(s))

def to_title_case(s: str) -> str:
    """
    Convert string to Title Case
    """
    return ' '.join(w.capitalize() for w in split_case_regex.split(s))

