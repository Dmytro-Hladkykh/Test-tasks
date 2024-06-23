#include <iostream>
#include <cassert>
#include <chrono>
#include "bigint.h"

using namespace std;

void test_arithmetic_operations() {
    BigInt a("123456789012345678901234567890");
    BigInt b("-987654321098765432109876543210");
    BigInt c("123456789012345678901234567890");

    assert((a + b) == BigInt("-864197532086419753208641975320"));
    assert((a - b) == BigInt("1111111110111111111011111111100"));
    assert((a / c) == BigInt("1"));
}

void test_multiplication() {
    BigInt a("123456789012345678901234567890");
    BigInt b("987654321098765432109876543210");
    
    auto start = chrono::high_resolution_clock::now();
    BigInt result_naive = a * b;
    auto end = chrono::high_resolution_clock::now();
    
    chrono::duration<double> diff_naive = end - start;
    
    start = chrono::high_resolution_clock::now();
    BigInt result_karatsuba = a.karatsuba(b);
    end = chrono::high_resolution_clock::now();
    
    chrono::duration<double> diff_karatsuba = end - start;
    
    cout << "Naive multiplication time: " << diff_naive.count() << " seconds" << endl;
    cout << "Karatsuba multiplication time: " << diff_karatsuba.count() << " seconds" << endl;
    
    assert(result_naive == result_karatsuba);
    assert(result_naive.toString() == "121932631137021795226185032733622923332237463801111263526900");
}

void test_exponentiation_and_modulus() {
    BigInt a("123456789012345678901234567890");
    BigInt b("3");
    BigInt c("987654321098765432109876543210");

    assert(a.pow(BigInt(2)) == BigInt("15241578753238836750495351562536198787501905199875019052100"));
    assert(a.pow(b) == BigInt("1881676372353657772546716040589641726257477229849409426207693797722198701224860897069000"));
    assert(c % b == BigInt("0"));
}

void test_comparison_operations() {
    BigInt a("123456789012345678901234567890");
    BigInt b("-987654321098765432109876543210");
    BigInt c("123456789012345678901234567890");

    assert(a > b);
    assert(b < c);
    assert(a == c);
    assert(a >= c);
    assert(b <= a);
    assert(a != b);
}

void test_conversions() {
    BigInt a("123456789");
    int b = a.toInt();
    assert(b == 123456789);
    
    BigInt c(-987654321);
    assert(c.toString() == "-987654321");
    
    try {
        BigInt d("1234567890123456789012345678901234567890");
        d.toInt();
        assert(false);  
    } catch (const overflow_error&) {
        cout << "toInt test passed" << endl;
    }
}

int main() {
    cout << "Running unit tests for BigInt class..." << endl;

    test_arithmetic_operations();
    test_multiplication();
    test_exponentiation_and_modulus();
    test_comparison_operations();
    test_conversions();

    cout << "All tests passed successfully!" << endl;

    return 0;
}
