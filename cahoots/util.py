"""
The MIT License (MIT)

Copyright (c) Serenity Software, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# pylint: disable=invalid-name


def truncate_text(text, limit=80):
    """
    truncates text to a provided length

    :param text: text we want to truncate
    :type text: str
    :param limit: how long we want the resulting string to be
    :type limit: int
    :return: truncated string
    :rtype: str
    """
    if len(text) > limit:
        text = text[:limit-3] + "..."
    return text


def is_number(text):
    """
    Checking if the text is a number

    :param text: text we want to examine
    :type text: str
    :return: whether this is a number or not
    :rtype: bool
    """
    try:
        float(text.strip())
    except ValueError:
        return False

    return True


def strings_intersect(s_one, s_two):
    """
    Checks if two strings have any intersections

    :param s_one: first string
    :type s_one: str
    :param s_two: second string
    :type s_two: str
    :return: whether or not these strings intercept
    :rtype: bool
    """
    return not set(s_one).isdisjoint(s_two)
