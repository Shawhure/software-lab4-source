#!/usr/bin/env python
import os
import sys
import time #fix bug 3


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pickbooksup.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

