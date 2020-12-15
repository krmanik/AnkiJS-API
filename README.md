# AnkiJS-API
Anki JavaScript API to get cards information in reviewer window

This addon is made to work with [AnkiDroid JS API]().

# Demo
![images](images/demo_1.png)

# To get card info in reviewer for creating decks
## New Card Count
```
pycmd("AnkiJS.ankiGetNewCardCount()", (ret) => {
    console.log(ret);
});
```

## Learn Card Count
```
pycmd("AnkiJS.ankiGetLrnCardCount()", (ret) => {
    console.log(ret);
});
```

## Review Card Count
```
pycmd("AnkiJS.ankiGetRevCardCount()", (ret) => {
    console.log(ret);
});
```

## Get Card Mark
```
pycmd("AnkiJS.ankiGetCardMark()", (ret) => {
    console.log(ret);
});
```

## Get Card Flag
```
pycmd("AnkiJS.ankiGetCardFlag()", (ret) => {
    console.log(ret);
});
```

## Get Card Id
```
pycmd("AnkiJS.ankiGetCardId()", (ret) => {
    console.log(ret);
});
```

## Get Card Type
```
pycmd("AnkiJS.ankiGetCardType()", (ret) => {
    console.log(ret);
});
```

## Get Next Time 1
```
pycmd("AnkiJS.ankiGetNextTime1()", (ret) => {
    console.log(ret);
});
```