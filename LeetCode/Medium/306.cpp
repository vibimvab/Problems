// Additive Number
// Medium

#include <string>
using namespace std;

/* first method, cannot solve with inputs larger than integer range
 * out_of_range error thrown at stoi function
bool isAdditiveNumber(string num) {
    int num1, num2, sum, sumLen, nextNum, loc;
    for (int num1Len = 1; num1Len < num.size(); num1Len++) {
        if (num1Len >= 2 && num[0] == '0') break;

        for (int num2Len = 1; num1Len + num2Len < num.size() && num1Len*2 <= num.size() && num2Len*2 <= num.size(); num2Len++) {
            if (num2Len >= 2 && num[num1Len] == '0') break;
            num1 = stoi(num.substr(0, num1Len));
            num2 = stoi(num.substr(num1Len, num2Len));

            sum = num1 + num2;
            if (sum > 0) sumLen = log10(sum) + 1;
            else sumLen = 1;

            for (loc = num1Len + num2Len; loc <= num.size();) {
                if (sumLen >= 2 && num[loc] == '0') {
                    break;
                }

                nextNum = stoi(num.substr(loc, sumLen));
                if (sum != nextNum) {
                    break;
                }

                if (loc + sumLen == num.size()) return true;

                loc += sumLen;
                num1 = num2;
                num2 = nextNum;
                sum = num1 + num2;
                if (sum > 0) sumLen = log10(sum) + 1;
                else sumLen = 1;
            }
        }
    }

    return false;
}
*/

// second method using string addition
string addStringNums(string a, string b) {
    auto aLen = a.size();
    auto bLen = b.size();
    string result = "";

    char n, m;
    char carry = 0;
    for (int i = 0; i < max(aLen, bLen); i++) {
        if (i < aLen) n = a[aLen-1-i] - 48; else n = 0;
        if (i < bLen) m = b[bLen-1-i] - 48; else m = 0;
        char sum = n + m + carry;
        if (sum >= 10) carry = 1; else carry = 0;
        result.push_back(sum % 10 + 48);
    }

    if (carry != 0) result.push_back(carry + 48);

    reverse(result.begin(), result.end());
    return result;
}

bool isAdditiveNumber(string num) {
    string num1, num2, sum, nextNum;
    int sumLen, loc;
    for (int num1Len = 1; num1Len < num.size(); num1Len++) {
        if (num[0] == '0' && num1Len >= 2) break;

        for (int num2Len = 1; num1Len + num2Len < num.size(); num2Len++) {
            if (num[num1Len] == '0' && num2Len >= 2) break;
            num1 = num.substr(0, num1Len);
            num2 = num.substr(num1Len, num2Len);

            sum = addStringNums(num1, num2);
            sumLen = sum.size();

            for (loc = num1Len + num2Len; loc < num.size();) {
                if (num[loc] == '0' && sumLen >= 2) break; // if next number has leading 0
                nextNum = num.substr(loc, sumLen);
                if (sum != nextNum) break; // if next number does not equal to the sum of the previous numbers

                if (loc + sumLen == num.size()) return true; // if the input string reaches the end

                loc += sumLen;
                num1 = num2;
                num2 = nextNum;
                sum = addStringNums(num1, num2);
                sumLen = sum.size();
            }
        }
    }

    return false;
}