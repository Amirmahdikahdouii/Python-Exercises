# Buy-Sell Stock

توی این برنامه از شما میخوایم که تعدادی اعداد که نمایانگر مقدار ارزش سهام توی هر ماه هستند(شماره ایندکس شماره ماه هر ارزش است!) را دریافت کنید و ماه یا ماه هایی که بیشترین بازدهی را داشته اند خروجی دهید.

**ورودی:**

در تنها خط ورودی برنامه به شما تعداد عدد داده میشود که نمایانگر ارزش آن ماه سهام است.


**خروجی:**

در تنها خط خروجی یک دیکشنری چاپ میکنید که به صورت زیر است.

```
{'high_profit': 0, 'months': []}
```

**نکته:**
در کلید high_profit مقدار بیشترین سود و در کلید month مقدار بیشترین ماه های سود آوری را چاپ میکنید

## Input-1:
```
7 1 5 3 6 4
```

## Output-1:
```
{'high_profit': 4, 'months': [1, 5]}
```

## Input-2:
```
7 1 5 3 6 4 8 10
```

## Output-2:
```
{'high_profit': 4, 'months': [[1, 5], [4, 8]]}
```

## Input-2:
```
9 8 7 4 3 2 1
```

## Output-2:
```
{'high_profit': 0, 'months': []}
```