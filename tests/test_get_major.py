# Test get_major() function
from .context import scrape_sic_osha as scrape


class TestClass:

    url = 'sic_manual.display?id=1&tab=group'
    major = scrape.get_major(url)

    def test_len(self):
        assert len(self.major) > 1

    def test_grapes(self):
        assert self.major[16].full_desc == \
            'SIC4 0172: Grapes'
        assert self.major[16].parent_desc == \
            'Industry Group 017: Fruits And Tree Nuts'

    def test_first(self):
        assert self.major[0].full_desc == \
            'Industry Group 011: Cash Grains'
        assert self.major[0].parent_desc == \
            'Major Group 01: Agricultural Production Crops'

    def test_last(self):
        assert self.major[len(self.major) - 1].full_desc == \
            'SIC4 0191: General Farms, Primarily Crop'
        assert self.major[len(self.major) - 1].parent_desc == \
            'Industry Group 019: General Farms, Primarily Crop'
