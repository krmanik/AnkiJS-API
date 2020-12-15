# AnkiJS-API
Anki JavaScript API to get cards information in reviewer window

This addon is made to work with [AnkiDroid JS API](https://github.com/ankidroid/Anki-Android/wiki/AnkiDroid-Javascript-API).

# Demo
![images](images/demo_1.png)

# To get card info in reviewer for creating decks
To know more about the options view
[AnkiDroid JS API](https://github.com/ankidroid/Anki-Android/wiki/AnkiDroid-Javascript-API).
## New Count
```
pycmd("AnkiJS.ankiGetNewCardCount()", (ret) => {
    console.log(ret);
});
```

## Learn Count
```
pycmd("AnkiJS.ankiGetLrnCardCount()", (ret) => {
    console.log(ret);
});
```

## Review Count
```
pycmd("AnkiJS.ankiGetRevCardCount()", (ret) => {
    console.log(ret);
});
```

## Mark
```
pycmd("AnkiJS.ankiGetCardMark()", (ret) => {
    console.log(ret);
});
```

## Flag
```
pycmd("AnkiJS.ankiGetCardFlag()", (ret) => {
    console.log(ret);
});
```

## Card Id
```
pycmd("AnkiJS.ankiGetCardId()", (ret) => {
    console.log(ret);
});
```

## Note Id
```
pycmd("AnkiJS.ankiGetCardNid()", (ret) => {
    console.log(ret);
});
```

## Deck Id
```
pycmd("AnkiJS.ankiGetCardDid()", (ret) => {
    console.log(ret);
});
```

## Last modified time of card
```
pycmd("AnkiJS.ankiGetCardMod()", (ret) => {
    console.log(ret);
});
```

## Type
```
pycmd("AnkiJS.ankiGetCardType()", (ret) => {
    console.log(ret);
});
```

## Queue
```
pycmd("AnkiJS.ankiGetCardQueue()", (ret) => {
    console.log(ret);
});
```

## Left
```
pycmd("AnkiJS.ankiGetCardLeft()", (ret) => {
    console.log(ret);
});
```

## Due
```
pycmd("AnkiJS.ankiGetCardDue()", (ret) => {
    console.log(ret);
});
```

## Interval
```
pycmd("AnkiJS.ankiGetCardInterval()", (ret) => {
    console.log(ret);
});
```

## Factor
```
pycmd("AnkiJS.ankiGetCardFactor()", (ret) => {
    console.log(ret);
});
```

## Reps
```
pycmd("AnkiJS.ankiGetCardReps()", (ret) => {
    console.log(ret);
});
```

## Lapses
```
pycmd("AnkiJS.ankiGetCardLapses()", (ret) => {
    console.log(ret);
});
```


## Original Due
```
pycmd("AnkiJS.ankiGetCardODue()", (ret) => {
    console.log(ret);
});
```

## Deck ID of home deck if filtered
```
pycmd("AnkiJS.ankiGetCardODid()", (ret) => {
    console.log(ret);
});
```


## Next Time 1
```
pycmd("AnkiJS.ankiGetNextTime1()", (ret) => {
    console.log(ret);
});
```

## Next Time 2
```
pycmd("AnkiJS.ankiGetNextTime2()", (ret) => {
    console.log(ret);
});
```

## Next Time 3
```
pycmd("AnkiJS.ankiGetNextTime3()", (ret) => {
    console.log(ret);
});
```

## Next Time 4
```
pycmd("AnkiJS.ankiGetNextTime4()", (ret) => {
    console.log(ret);
});
```