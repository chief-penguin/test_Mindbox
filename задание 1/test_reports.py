from pandas.util.testing import assert_frame_equal
from create_report_func import create_report

class ProductsTest(unittest.TestCase):
    def test_df(self):
        df1 = create_report(pd.read_csv('orders1.csv'), pd.read_csv('order_lines1.csv'))
        assert_frame_equal(df1, pd.read_csv('report1.csv', index_col=0))
        
        df2 = create_report(pd.read_csv('orders2.csv'), pd.read_csv('order_lines2.csv'))
        assert_frame_equal(df2, pd.read_csv('report2.csv', index_col=0), check_index_type=False, check_dtype=False)
        
        df3 = create_report(pd.read_csv('orders3.csv'), pd.read_csv('order_lines3.csv'))
        assert_frame_equal(df3, pd.read_csv('report3.csv', index_col=0), check_index_type=False, check_dtype=False)
        
        df4 = create_report(pd.read_csv('orders4.csv'), pd.read_csv('order_lines4.csv'))
        assert_frame_equal(df4, pd.read_csv('report4.csv', index_col=0), check_index_type=False, check_dtype=False)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ProductsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)