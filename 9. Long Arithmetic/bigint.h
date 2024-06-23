#ifndef BIGINT_H
#define BIGINT_H

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdexcept>
#include <cstdint>
#include <climits>
#include <complex>

class BigInt {
private:
    std::vector<uint32_t> digits; // Vector to store the digits of the BigInt
    bool negative; // Sign of the BigInt (true if negative, false if non-negative)

    // Private utility function to remove unnecessary leading zeros from digits
    void removeLeadingZeros();

    // Private static utility function for naive multiplication of two BigInts
    static BigInt naiveMultiply(const BigInt& a, const BigInt& b);

public:
    // Constructors
    BigInt(); // Default constructor initializes BigInt to 0
    BigInt(const std::string& str); // Constructor to initialize BigInt from string
    BigInt(int64_t num); // Constructor to initialize BigInt from int64_t

    // Unary arithmetic operators
    BigInt operator-() const; // Unary negation
    BigInt abs() const; // Returns the absolute value of the BigInt

    // Compound assignment operators
    BigInt& operator+=(const BigInt& rhs); // Addition assignment
    BigInt& operator-=(const BigInt& rhs); // Subtraction assignment
    BigInt& operator*=(const BigInt& rhs); // Multiplication assignment
    BigInt& operator/=(const BigInt& rhs); // Division assignment
    BigInt& operator%=(const BigInt& rhs); // Modulo assignment

    // Binary arithmetic operators
    BigInt operator+(const BigInt& rhs) const; // Addition
    BigInt operator-(const BigInt& rhs) const; // Subtraction
    BigInt operator*(const BigInt& rhs) const; // Multiplication
    BigInt operator/(const BigInt& rhs) const; // Division
    BigInt operator%(const BigInt& rhs) const; // Modulo

    // Comparison operators
    bool operator<(const BigInt& rhs) const; // Less than
    bool operator>(const BigInt& rhs) const; // Greater than
    bool operator<=(const BigInt& rhs) const; // Less than or equal to
    bool operator>=(const BigInt& rhs) const; // Greater than or equal to
    bool operator==(const BigInt& rhs) const; // Equal to
    bool operator!=(const BigInt& rhs) const; // Not equal to

    // Bitwise shift operators
    BigInt operator<<(int shift) const; // Left shift
    BigInt operator>>(int shift) const; // Right shift
    BigInt& operator<<=(int shift); // Left shift assignment
    BigInt& operator>>=(int shift); // Right shift assignment

    // Stream insertion and extraction operators
    friend std::ostream& operator<<(std::ostream& os, const BigInt& bi); // Output to stream
    friend std::istream& operator>>(std::istream& is, BigInt& bi); // Input from stream

    // Other member functions
    std::string toString() const; // Convert BigInt to string
    int toInt() const; // Convert BigInt to int
    bool isZero() const; // Check if BigInt is zero
    BigInt pow(const BigInt& exponent) const; // BigInt exponentiation

    // Karatsuba multiplication algorithm
    BigInt karatsuba(const BigInt& rhs) const;

};

BigInt::BigInt() : negative(false) {
    digits.push_back(0);
}

BigInt::BigInt(const std::string& str) : negative(false) {
    if (str.empty()) {
        digits.push_back(0);
        return;
    }

    size_t start = 0;
    if (str[0] == '-') {
        negative = true;
        start = 1;
    } else if (str[0] == '+') {
        start = 1;
    }

    for (size_t i = str.length() - 1; i >= start; i -= 9) {
        uint32_t digit = 0;
        for (int j = std::max(static_cast<int>(start), static_cast<int>(i) - 8); j <= static_cast<int>(i); ++j) {
            digit = digit * 10 + (str[j] - '0');
        }
        digits.push_back(digit);
        if (i < 9) break;
    }

    removeLeadingZeros();
}

BigInt::BigInt(int64_t num) : negative(num < 0) {
    num = std::abs(num);
    do {
        digits.push_back(num % 1000000000);
        num /= 1000000000;
    } while (num > 0);
}

void BigInt::removeLeadingZeros() {
    while (digits.size() > 1 && digits.back() == 0) {
        digits.pop_back();
    }
    if (digits.size() == 1 && digits[0] == 0) {
        negative = false;
    }
}

BigInt BigInt::operator-() const {
    BigInt result = *this;
    if (!isZero()) {
        result.negative = !result.negative;
    }
    return result;
}

BigInt BigInt::abs() const {
    BigInt result = *this;
    result.negative = false;
    return result;
}

BigInt& BigInt::operator+=(const BigInt& rhs) {
    if (negative != rhs.negative) {
        return *this -= (-rhs);
    }

    digits.resize(std::max(digits.size(), rhs.digits.size()), 0);
    uint64_t carry = 0;
    for (size_t i = 0; i < digits.size(); ++i) {
        uint64_t sum = carry + digits[i] + (i < rhs.digits.size() ? rhs.digits[i] : 0);
        digits[i] = static_cast<uint32_t>(sum % 1000000000);
        carry = sum / 1000000000;
    }
    if (carry) digits.push_back(carry);

    removeLeadingZeros();
    return *this;
}

BigInt& BigInt::operator-=(const BigInt& rhs) {
    if (negative != rhs.negative) {
        return *this += (-rhs);
    }

    if (abs() < rhs.abs()) {
        *this = -(rhs - *this);
        return *this;
    }

    uint64_t borrow = 0;
    for (size_t i = 0; i < digits.size(); ++i) {
        int64_t diff = static_cast<int64_t>(digits[i]) - borrow - (i < rhs.digits.size() ? rhs.digits[i] : 0);
        if (diff < 0) {
            diff += 1000000000;
            borrow = 1;
        } else {
            borrow = 0;
        }
        digits[i] = static_cast<uint32_t>(diff);
    }

    removeLeadingZeros();
    return *this;
}

BigInt BigInt::naiveMultiply(const BigInt& a, const BigInt& b) {
    BigInt result;
    result.digits.resize(a.digits.size() + b.digits.size());

    for (size_t i = 0; i < a.digits.size(); ++i) {
        uint64_t carry = 0;
        for (size_t j = 0; j < b.digits.size() || carry; ++j) {
            uint64_t current = result.digits[i + j] +
                               static_cast<uint64_t>(a.digits[i]) * (j < b.digits.size() ? b.digits[j] : 0) +
                               carry;
            result.digits[i + j] = static_cast<uint32_t>(current % 1000000000);
            carry = current / 1000000000;
        }
    }

    result.negative = a.negative != b.negative;
    result.removeLeadingZeros();
    return result;
}

BigInt& BigInt::operator*=(const BigInt& rhs) {
    *this = naiveMultiply(*this, rhs);
    return *this;
}

BigInt& BigInt::operator/=(const BigInt& rhs) {
    if (rhs.isZero()) {
        throw std::runtime_error("Division by zero");
    }

    BigInt quotient;
    BigInt remainder = this->abs();
    BigInt divisor = rhs.abs();

    if (remainder < divisor) {
        *this = BigInt(0);
        return *this;
    }

    int shift = 0;
    while ((divisor << shift) <= remainder) {
        shift++;
    }
    shift--;

    for (int i = shift; i >= 0; i--) {
        if ((divisor << i) <= remainder) {
            remainder -= (divisor << i);
            quotient.digits[i / 32] |= (1U << (i % 32));
        }
    }

    quotient.negative = (this->negative != rhs.negative) && !quotient.isZero();
    quotient.removeLeadingZeros();
    *this = quotient;
    return *this;
}

BigInt& BigInt::operator%=(const BigInt& rhs) {
    if (rhs.isZero()) {
        throw std::runtime_error("Modulo by zero");
    }

    BigInt absThis = this->abs();
    BigInt absRhs = rhs.abs();

    while (absThis >= absRhs) {
        int shift = 0;
        while ((absRhs << shift) <= absThis) {
            shift++;
        }
        shift--;
        absThis -= (absRhs << shift);
    }

    *this = absThis;
    if (negative) {
        *this = rhs.abs() - *this;
    }
    return *this;
}

BigInt BigInt::operator+(const BigInt& rhs) const {
    BigInt result = *this;
    result += rhs;
    return result;
}

BigInt BigInt::operator-(const BigInt& rhs) const {
    BigInt result = *this;
    result -= rhs;
    return result;
}

BigInt BigInt::operator*(const BigInt& rhs) const {
    return naiveMultiply(*this, rhs);
}

BigInt BigInt::operator/(const BigInt& rhs) const {
    BigInt result = *this;
    result /= rhs;
    return result;
}

BigInt BigInt::operator%(const BigInt& rhs) const {
    BigInt result = *this;
    result %= rhs;
    return result;
}

bool BigInt::operator<(const BigInt& rhs) const {
    if (negative != rhs.negative) return negative;
    if (digits.size() != rhs.digits.size())
        return negative ? (digits.size() > rhs.digits.size()) : (digits.size() < rhs.digits.size());
    for (int i = digits.size() - 1; i >= 0; --i) {
        if (digits[i] != rhs.digits[i])
            return negative ? (digits[i] > rhs.digits[i]) : (digits[i] < rhs.digits[i]);
    }
    return false;
}

bool BigInt::operator>(const BigInt& rhs) const {
    return rhs < *this;
}

bool BigInt::operator<=(const BigInt& rhs) const {
    return !(rhs < *this);
}

bool BigInt::operator>=(const BigInt& rhs) const {
    return !(*this < rhs);
}

bool BigInt::operator==(const BigInt& rhs) const {
    return (negative == rhs.negative) && (digits == rhs.digits);
}

bool BigInt::operator!=(const BigInt& rhs) const {
    return !(*this == rhs);
}

BigInt BigInt::operator<<(int shift) const {
    BigInt result = *this;
    if (shift == 0 || isZero()) return result;

    int digitShift = shift / 9;
    int bitShift = shift % 9;

    if (digitShift > 0) {
        result.digits.insert(result.digits.begin(), digitShift, 0);
    }

    if (bitShift > 0) {
        uint64_t carry = 0;
        for (size_t i = 0; i < result.digits.size(); ++i) {
            uint64_t current = result.digits[i];
            current = (current << bitShift) | carry;
            result.digits[i] = static_cast<uint32_t>(current % 1000000000);
            carry = current / 1000000000;
        }
        if (carry) result.digits.push_back(carry);
    }

    result.removeLeadingZeros();
    return result;
}

BigInt BigInt::operator>>(int shift) const {
    BigInt result = *this;
    if (shift == 0 || isZero()) return result;

    int digitShift = shift / 9;
    int bitShift = shift % 9;

    if (digitShift >= static_cast<int>(result.digits.size())) {
        result.digits = {0};
        return result;
    }

    result.digits.erase(result.digits.begin(), result.digits.begin() + digitShift);

    if (bitShift > 0) {
        uint64_t carry = 0;
        for (int i = result.digits.size() - 1; i >= 0; --i) {
            uint64_t current = result.digits[i];
            uint64_t next_carry = current & ((1 << bitShift) - 1);
            current = (current >> bitShift) | (carry << (9 - bitShift));
            result.digits[i] = static_cast<uint32_t>(current);
            carry = next_carry;
        }
    }

    result.removeLeadingZeros();
    return result;
}

BigInt& BigInt::operator<<=(int shift) {
    *this = *this << shift;
    return *this;
}

BigInt& BigInt::operator>>=(int shift) {
    *this = *this >> shift;
    return *this;
}

std::string BigInt::toString() const {
    if (isZero()) return "0";

    std::string result;
    if (negative) result += "-";

    result += std::to_string(digits.back());
    for (int i = static_cast<int>(digits.size()) - 2; i >= 0; --i) {
        std::string digit = std::to_string(digits[i]);
        result += std::string(9 - digit.length(), '0') + digit;
    }

    return result;
}

int BigInt::toInt() const {
    if (*this > BigInt(INT_MAX) || *this < BigInt(INT_MIN)) {
        throw std::overflow_error("BigInt value does not fit into int");
    }
    return std::stoi(this->toString());
}

bool BigInt::isZero() const {
    return (digits.size() == 1 && digits[0] == 0) || digits.empty();
}

BigInt BigInt::pow(const BigInt& exponent) const {
    if (exponent.negative) {
        throw std::runtime_error("Negative exponent is not supported");
    }

    BigInt result(1);
    BigInt base = *this;
    BigInt exp = exponent;

    while (!exp.isZero()) {
        if (exp.digits[0] & 1) {
            result *= base;
        }
        base *= base;
        exp = exp >> 1;  
    }

    return result;
}

BigInt BigInt::karatsuba(const BigInt& rhs) const {
    const BigInt& a = *this;
    const BigInt& b = rhs;

    if (a.digits.size() < 64 || b.digits.size() < 64) {
        return naiveMultiply(a, b);
    }

    size_t n = std::max(a.digits.size(), b.digits.size());
    size_t m = n / 2;

    BigInt high1 = a >> (m * 32);
    BigInt low1 = a - (high1 << (m * 32));
    BigInt high2 = b >> (m * 32);
    BigInt low2 = b - (high2 << (m * 32));

    BigInt z0 = low1.karatsuba(low2);
    BigInt z1 = (low1 + high1).karatsuba(low2 + high2);
    BigInt z2 = high1.karatsuba(high2);

    BigInt result = (z2 << (2 * m * 32)) + ((z1 - z2 - z0) << (m * 32)) + z0;
    result.negative = a.negative != b.negative;
    result.removeLeadingZeros();
    return result;
}

std::ostream& operator<<(std::ostream& os, const BigInt& bi) {
    os << bi.toString();
    return os;
}

std::istream& operator>>(std::istream& is, BigInt& bi) {
    std::string str;
    is >> str;
    bi = BigInt(str);
    return is;
}

#endif // BIGINT_H