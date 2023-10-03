# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_gws import GWS


def get_group_members(group_id):
    group_members = {}
    for member in GWS().get_effective_members(group_id):
        if member.is_uwnetid():
            group_members['{}@uw.edu'.format(member.name)] = True
    return group_members
