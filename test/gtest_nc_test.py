#!/usr/bin/env python
#
# Copyright 2007, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Negative compilation test for Google Test."""

__author__ = 'wan@google.com (Zhanyong Wan)'

import os
import sys
import unittest


class GTestNCTest(unittest.TestCase):
  """Negative compilation test for Google Test."""

  def testCompilerError(self):
    """Verifies that erroneous code leads to expected compiler
    messages."""

    # Defines a list of test specs, where each element is a tuple
    # (test name, list of regexes for matching the compiler errors).
    test_specs = [
      ('CANNOT_IGNORE_RUN_ALL_TESTS_RESULT',
       [r'ignoring return value']),

      ('USER_CANNOT_INCLUDE_GTEST_INTERNAL_INL_H',
       [r'must not be included except by Google Test itself']),

      ('CATCHES_DECLARING_SETUP_IN_TEST_FIXTURE_WITH_TYPO',
       [r'Setup_should_be_spelled_SetUp']),

      ('CATCHES_CALLING_SETUP_IN_TEST_WITH_TYPO',
       [r'Setup_should_be_spelled_SetUp']),

      ('CATCHES_DECLARING_SETUP_IN_ENVIRONMENT_WITH_TYPO',
       [r'Setup_should_be_spelled_SetUp']),

      ('CATCHES_CALLING_SETUP_IN_ENVIRONMENT_WITH_TYPO',
       [r'Setup_should_be_spelled_SetUp']),

      ('SANITY',
       None)
      ]

    # TODO(wan@google.com): verify that the test specs are satisfied.


if __name__ == '__main__':
  unittest.main()
