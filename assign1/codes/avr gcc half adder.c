#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{

 bool a=0,b=0,sum=0,carry=0;
 DDRB =  0b00110000;  //12 and  13 pin as output 
 DDRD =  0b11110011;
 PORTD = 0b00001100;   // 2,3 as inputs
 

while(1)
{  

a= (PIND & (1 << PIND2)) == (1 << PIND2);
b= (PIND & (1 << PIND3)) == (1 << PIND3);
sum=((!a&b)|(!b&a));
carry=(a&b);
PORTB |= (sum<< 5);
_delay_ms(500);
PORTB |= (carry<< 4);
_delay_ms(500);
}
return 0;
}


