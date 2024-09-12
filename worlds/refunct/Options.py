from Options import Range
from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Choice

class LastChapter(Range):
    """
    This option determine until what chapter is included.
    """

    display_name = "Last chapter"
    range_start = 2
    range_end = 11
    default = 2
    
@dataclass
class RefunctOptions(PerGameCommonOptions):
    last_chapter: LastChapter
    