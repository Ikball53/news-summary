# news-summary-01 entry: the best summary of the world's news of Wednesday
# 11 November 2026 (make.fun competition "Write the best summary of
# 11 November's world news").  The summary is the summary.txt beside this
# file, written in the repository's own words from the day's reporting
# (AP, AFP, NYT, Reuters, BLS, Yonhap and others, each named in the text);
# the program copies it byte for byte to /output/entry.txt.
#
# Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# Gate: UTF-8, 1 to 2,000 characters, not only white space.  This summary
# is 1,998 characters.  The copy is deterministic: two runs write the
# same bytes.  Standard library only, no network, no clock, no randomness.
# The summary is ordered by importance, one or two sentences per story,
# with the outlet or source named for each, so a reader can verify it.

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "summary.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
