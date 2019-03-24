#include <stdio.h>
#include <stdint.h>

#define TEN_BILLION (10000000000)

int main()
{
    uint64_t prime = 1;
    for (uint32_t i = 1; i <= 7830457; i++)
    {
        // multiply by 2 but only keep the 10th last digits
        prime = (2*prime) % TEN_BILLION;
    }

    prime = (28433 * prime + 1) % TEN_BILLION;

    printf("The last 10 digits are: %lld\n", prime);
}