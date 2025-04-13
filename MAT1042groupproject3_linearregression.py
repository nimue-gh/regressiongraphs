
"""
Created on Sat Apr 12 15:08:46 2025
"""
import numpy as np
import matplotlib.pyplot as plot
    
time_m100 = np.array([
    10.60,
    10.40,
    10.30,
    10.20,
    10.10,
    10.00,
    9.99,
    9.95,
    9.93,
    9.92,
    9.90,
    9.86,
    9.85,
    9.84,
    9.79,
    9.78,
    9.77,
    9.74,
    9.72,
    9.69,
    9.58
])
year_m100 = np.array([
    1912,
    1921,
    1930,
    1936,
    1956,
    1960,
    1968,
    1968,
    1983,
    1988,
    1991,
    1991,
    1994,
    1996,
    1999,
    2002,
    2005,
    2007,
    2008,
    2008,
    2009,
])

time_f100 = np.array([
    13.60,
    12.80,
    12.70,
    12.80,
    12.40,
    12.20,
    12.40,
    12.20,
    12.10,
    12.20,
    12.00,
    12.00,
    12.00,
    12.00,
    11.90,
    11.90,
    11.90,
    11.80,
    11.90,
    11.70,
    11.90,
    11.80,
    11.60,
    11.50,
    11.60,
    11.50,
    11.50,
    11.50,
    11.50,
    11.50,
    11.40,
    11.30,
    11.30,
    11.30,
    11.20,
    11.20,
    11.10,
    11.10,
    11.10,
    11.10,
    11.10,
    11.10,
    11.10,
    11.10,
    11.00,
    11.00,
    11.00,
    11.00,
    11.00,
    11.00,
    11.00,
    10.90,
    10.90,
    10.80,
    11.07,
    11.07,
    11.04,
    11.01,
    10.88,
    10.88,
    10.81,
    10.79,
    10.76,
    10.49
])
year_f100 = np.array([
    1922,
    1922,
    1923,
    1923,
    1925,
    1925,
    1926,
    1926,
    1927,
    1928,
    1928,
    1928,
    1931,
    1930,
    1932,
    1932,
    1932,
    1933,
    1934,
    1934,
    1935,
    1935,
    1935,
    1936,
    1937,
    1939,
    1939,
    1943,
    1948,
    1952,
    1952,
    1955,
    1958,
    1960,
    1961,
    1964,
    1965,
    1965,
    1967,
    1968,
    1968,
    1968,
    1968,
    1968,
    1968,
    1970,
    1970,
    1971,
    1972,
    1972,
    1972,
    1973,
    1973,
    1973,
    1968,
    1972,
    1976,
    1976,
    1977,
    1982,
    1983,
    1983,
    1984,
    1988
])


time_m1500 = np.array([
    235.8,
    234.7,
    232.6,
    231.0,
    229.2,
    229.2,
    229.0,
    228.8,
    227.8,
    227.6,
    225.8,
    225.0,
    223.0,
    223.0,
    223.0,
    222.8,
    221.8,
    220.8,
    220.8,
    220.8,
    220.6,
    220.2,
    220.2,
    218.1,
    216.0,
    215.6,
    213.1,
    212.2,
    212.1,
    212.1,
    211.4,
    211.1,
    210.8,
    209.7,
    209.5,
    208.9,
    207.4,
    206.0
])
year_m1500 = np.array([
    1912,
    1917,
    1924,
    1926,
    1930,
    1933,
    1933,
    1934,
    1936,
    1941,
    1942,
    1943,
    1944,
    1947,
    1952,
    1954,
    1954,
    1955,
    1955,
    1955,
    1956,
    1957,
    1957,
    1957,
    1958,
    1960,
    1967,
    1974,
    1979,
    1980,
    1980,
    1983,
    1983,
    1985,
    1985,
    1992,
    1995,
    1998
])

time_f1500 = np.array([
    318.2,
    307,
    302,
    287.2,
    285.2,
    281.8,
    278,
    277.8,
    277,
    275.4,
    270,
    269.7,
    259,
    257.3,
    255.6,
    252.4,
    250.7,
    249.6,
    246.9,
    246.5,
    245.1,
    241.4,
    236,
    235,
    232.5,
    230.5,
    230.1
])
year_f1500 = np.array([
    1927,
    1934,
    1936,
    1936,
    1937,
    1940,
    1944,
    1946,
    1952,
    1956,
    1957,
    1957,
    1962,
    1967,
    1967,
    1969,
    1969,
    1971,
    1972,
    1972,
    1972,
    1972,
    1976,
    1980,
    1980,
    1993,
    2015
])


dist_mLJ = np.array([
    7.61,
    7.69,
    7.76,
    7.89,
    7.90,
    7.93,
    7.98,
    8.13,
    8.21,
    8.24,
    8.28,
    8.31,
    8.31,
    8.34,
    8.35,
    8.35,
    8.90,
    8.95
])
year_mLJ = np.array([
    1901,
    1923,
    1924,
    1925,
    1928,
    1928,
    1931,
    1935,
    1960,
    1961,
    1961,
    1962,
    1964,
    1964,
    1965,
    1967,
    1968,
    1991
])

dist_fLJ = np.array([
    5.16,
    5.30,
    5.485,
    5.50,
    5.57,
    5.98,
    6.12,
    6.25,
    6.28,
    6.28,
    6.31,
    6.35,
    6.35,
    6.40,
    6.42,
    6.48,
    6.53,
    6.70,
    6.76,
    6.82,
    6.84,
    6.92,
    6.99,
    7.07,
    7.09,
    7.15,
    7.20,
    7.21,
    7.27,
    7.43,
    7.44,
    7.45,
    7.45,
    7.45,
    7.45,
    7.52
])
year_fLJ = np.array([
    1922,
    1923,
    1926,
    1926,
    1927,
    1928,
    1939,
    1943,
    1954,
    1955,
    1955,
    1956,
    1956,
    1960,
    1961,
    1961,
    1962,
    1964,
    1964,
    1968,
    1970,
    1976,
    1976,
    1978,
    1978,
    1982,
    1982,
    1983,
    1983,
    1983,
    1985,
    1986,
    1986,
    1987,
    1988,
    1988
])


dist_mHJ = np.array([
    2.00,
    2.01,
    2.02,
    2.03,
    2.04,
    2.06,
    2.07,
    2.08,
    2.09,
    2.10,
    2.11,
    2.12,
    2.15,
    2.16,
    2.17,
    2.18,
    2.19,
    2.22,
    2.23,
    2.24,
    2.25,
    2.26,
    2.27,
    2.28,
    2.29,
    2.30,
    2.31,
    2.32,
    2.33,
    2.34,
    2.35,
    2.36,
    2.37,
    2.38,
    2.39,
    2.40,
    2.41,
    2.42,
    2.43,
    2.44,
    2.45
])
year_mHJ = np.array([
    1912,
    1914,
    1917,
    1924,
    1933,
    1934,
    1936,
    1937,
    1937,
    1941,
    1941,
    1953,
    1956,
    1957,
    1960,
    1960,
    1960,
    1960,
    1961,
    1961,
    1961,
    1962,
    1962,
    1963,
    1970,
    1973,
    1976,
    1976,
    1977,
    1978,
    1980,
    1980,
    1983,
    1983,
    1984,
    1985,
    1985,
    1987,
    1988,
    1989,
    1993
])

dist_fHJ = np.array([
    1.46,
    1.485,
    1.485,
    1.524,
    1.552,
    1.58,
    1.58,
    1.595,
    1.605,
    1.62,
    1.65,
    1.65,
    1.66,
    1.66,
    1.66,
    1.71,
    1.72,
    1.73,
    1.74,
    1.75,
    1.76,
    1.76,
    1.77,
    1.78,
    1.8,
    1.81,
    1.82,
    1.83,
    1.84,
    1.85,
    1.86,
    1.87,
    1.88,
    1.9,
    1.91,
    1.92,
    1.92,
    1.94,
    1.94,
    1.95,
    1.96,
    1.96,
    1.97,
    1.97,
    2,
    2.01,
    2.01,
    2.02,
    2.03,
    2.03,
    2.04,
    2.05,
    2.07,
    2.07,
    2.08,
    2.09
])
year_fHJ = np.array([
    1922,
    1923,
    1923,
    1925,
    1926,
    1926,
    1928,
    1928,
    1929,
    1932,
    1932,
    1932,
    1939,
    1941,
    1941,
    1943,
    1951,
    1954,
    1956,
    1956,
    1956,
    1957,
    1957,
    1958,
    1958,
    1958,
    1958,
    1958,
    1959,
    1960,
    1960,
    1961,
    1961,
    1961,
    1961,
    1971,
    1972,
    1972,
    1974,
    1974,
    1976,
    1977,
    1977,
    1977,
    1977,
    1978,
    1978,
    1982,
    1983,
    1983,
    1983,
    1984,
    1984,
    1986,
    1986,
    1987
])


time_mMT = np.array([
    10518,
    10365,
    10013,
    9965,
    9751,
    9634,
    9496,
    9367,
    9156,
    8942,
    8869,
    8804,
    8802,
    8707,
    8442,
    8320,
    8315,
    8259,
    8177,
    8116,
    8116,
    8068,
    8035,
    7931,
    7920,
    7776,
    7714,
    7698,
    7685,
    7632,
    7610,
    7565,
    7542,
    7538,
    7495,
    7466,
    7439,
    7418,
    7403,
    7377
])
year_mMT = np.array([
    1908,
    1909,
    1909,
    1909,
    1909,
    1909,
    1913,
    1913,
    1920,
    1925,
    1935,
    1935,
    1935,
    1947,
    1952,
    1953,
    1953,
    1954,
    1958,
    1960,
    1963,
    1963,
    1964,
    1964,
    1965,
    1967,
    1969,
    1981,
    1984,
    1985,
    1988,
    1998,
    1999,
    2002,
    2003,
    2007,
    2008,
    2011,
    2013,
    2014
])

time_fMT = np.array([
    10973,
    9990,
    10545,
    9996,
    9835,
    9499,
    9551,
    9288,
    9150,
    8853,
    8742,
    8806,
    8771,
    8563,
    8666,
    8466,
    8694,
    8568,
    8631,
    8673,
    8724,
    8658,
    8623,
    8647,
    8505,
    8711,
    8764,
    8527,
    8447,
    8443,
    8493,
    8327,
    8238,
    8125,
    8381,
    8262,
    8376,
    8438,
    8359,
    8531,
    8425,
    8300,
    8317,
    8397,
    8418
])
year_fMT = np.array([
    1970,
    1971,
    1972,
    1973,
    1974,
    1975,
    1976,
    1977,
    1978,
    1979,
    1980,
    1981,
    1982,
    1983,
    1984,
    1985,
    1986,
    1987,
    1988,
    1989,
    1990,
    1991,
    1992,
    1993,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999,
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014
    ])

def records_100m():
    x0 = np.ones(21)
    X = np.column_stack((x0, year_m100))
    beta = (np.linalg.inv(np.transpose(X)@X))@np.transpose(X)@time_m100
    time_m100_predict = beta[0] + year_m100*beta[1]
    
    plot.plot(year_m100, time_m100, 'ro', label = "Year of record/Record time")
    plot.plot(year_m100, time_m100_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Male 100m record progression by year')
    plot.show()


    x1 = np.ones(64)
    X2 = np.column_stack((x1, year_f100))
    beta2 = (np.linalg.inv(np.transpose(X2)@X2))@np.transpose(X2)@time_f100
    time_f100_predict = beta2[0] + year_f100*beta2[1]
    
    plot.plot(year_f100, time_f100, 'ro', label = "Year of record/Record time")
    plot.plot(year_f100, time_f100_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Female 100m record progression by year')
    plot.show()

def records_1500m():
    x0 = np.ones(38)
    X = np.column_stack((x0, year_m1500))
    beta = (np.linalg.inv(np.transpose(X)@X))@np.transpose(X)@time_m1500
    time_m1500_predict = beta[0]+ year_m1500*beta[1]
    
    plot.plot(year_m1500, time_m1500, 'ro', label = "Year of record/Record time")
    plot.plot(year_m1500, time_m1500_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Male 1500m record progression by year')
    plot.show()
    
    
    x1 = np.ones(27)
    X2 = np.column_stack((x1, year_f1500))
    beta2 = (np.linalg.inv(np.transpose(X2)@X2))@np.transpose(X2)@time_f1500
    time_f1500_predict = beta2[0] + year_f1500*beta2[1]
    
    plot.plot(year_f1500, time_f1500, 'ro', label = "Year of record/Record time")
    plot.plot(year_f1500, time_f1500_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Female 100m record progression by year')
    plot.show()
    
def records_LJ():
    x0 = np.ones(18)
    X = np.column_stack((x0, year_mLJ))
    beta = (np.linalg.inv(np.transpose(X)@X))@np.transpose(X)@dist_mLJ
    dist_mLJ_predict = beta[0] + year_mLJ*beta[1]
    
    plot.plot(year_mLJ, dist_mLJ, 'ro', label = "Year of record/Record distance")
    plot.plot(year_mLJ, dist_mLJ_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record distance /m')
    plot.legend()
    plot.title('Male long jump record progression by year')
    plot.show()


    x1 = np.ones(36)
    X2 = np.column_stack((x1, year_fLJ))
    beta2 = (np.linalg.inv(np.transpose(X2)@X2))@np.transpose(X2)@dist_fLJ
    dist_fLJ_predict = beta2[0] + year_fLJ*beta2[1]
    
    plot.plot(year_fLJ, dist_fLJ, 'ro', label = "Year of record/Record distance")
    plot.plot(year_fLJ, dist_fLJ_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record distance /m')
    plot.legend()
    plot.title('Female long jump record progression by year')
    plot.show()
    
def records_HJ():
    x0 = np.ones(41)
    X = np.column_stack((x0, year_mHJ))
    beta = (np.linalg.inv(np.transpose(X)@X))@np.transpose(X)@dist_mHJ
    dist_mHJ_predict = beta[0] + year_mHJ*beta[1]
    
    plot.plot(year_mHJ, dist_mHJ, 'ro', label = "Year of record/Record height")
    plot.plot(year_mHJ, dist_mHJ_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record height /m')
    plot.legend()
    plot.title('Male high jump record progression by year')
    plot.show()


    x1 = np.ones(56)
    X2 = np.column_stack((x1, year_fHJ))
    beta2 = (np.linalg.inv(np.transpose(X2)@X2))@np.transpose(X2)@dist_fHJ
    dist_fHJ_predict = beta2[0] + year_fHJ*beta2[1]
    
    plot.plot(year_fHJ, dist_fHJ, 'ro', label = "Year of record/Record height")
    plot.plot(year_fHJ, dist_fHJ_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record height /m')
    plot.legend()
    plot.title('Female height jump record progression by year')
    plot.show()

def records_MT():
    x0 = np.ones(40)
    X = np.column_stack((x0, year_mMT))
    beta = (np.linalg.inv(np.transpose(X)@X))@np.transpose(X)@time_mMT
    time_mMT_predict = beta[0] + year_mMT*beta[1]
    
    plot.plot(year_mMT, time_mMT, 'ro', label = "Year of record/Record time")
    plot.plot(year_mMT, time_mMT_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Male marathon record progression by year')
    plot.show()


    x1 = np.ones(45)
    X2 = np.column_stack((x1, year_fMT))
    beta2 = (np.linalg.inv(np.transpose(X2)@X2))@np.transpose(X2)@time_fMT
    time_fMT_predict = beta2[0] + year_fMT*beta2[1]
    
    plot.plot(year_fMT, time_fMT, 'ro', label = "Year of record/Record time")
    plot.plot(year_fMT, time_fMT_predict, label = 'Approximate correlation')
    plot.xlabel('Year of record')
    plot.ylabel('Record time /s')
    plot.legend()
    plot.title('Female marathon record progression by year')
    plot.show()
    
records_100m()
records_1500m()
records_LJ()
records_HJ()
records_MT()