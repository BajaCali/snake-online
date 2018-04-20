# Messages format and communication

## Server -> Client

Ze serveru jdou vždy dvě zprávy po sobě, kde první obsahuje právě délku zprávy druhé.

| num  | len     | name         | format of payload    | description                                               |
| ---: | ------- | ------------ | -------------------- | --------------------------------------------------------- |
| 1.   | 4       | délka zpravy | number in string     | posílá délku další zpravy s kontextem                     |
| 2.   | dynamic | data         | dictionary in string | posíla slovník jako pole znaků, slovník obsahuje data hry |

##### Legenda

num - pořadí (posílání zpráv je cyklické)
len - délká zprávy
name - zkrácený název zprávy
format of payload - formát obsahu
description - stručný popis

### Format of data

| name in dic | format                 | description                                                |
| ----------- | ---------------------- | ---------------------------------------------------------- |
| map         | list of lists of chars | the game field of things on the map, for more read farther |
| x           | int                    | width of map                                               |
| y           | int                    | height of map                                              |
| snakes      | int                    | number of snakes in game                                   |
| a           | dic                    | informations about one of the snakes                       |

#### Format of snakes' dic

| name in dic | format              | description                                         |
| ----------- | ------------------- | --------------------------------------------------- |
| name        | string              | name of snake                                       |
| color       | tuple of size three | (e.g. (255, 50, 0)) in RGB format - colour of snake |
| score       | int                 | actual score of snake                               |

## Client -> Server

Dva typy zpráv:

2. inicializace hada jako takového formátově podobně jako Format of snakes' dic
1. direction formát v podobě jednoho znaku - int
    - 1 = NORTH
    - 2 = SOUTH
    - 3 = EAST
    - 4 = WEST
- pro připojení nového hada nuto zaslat číslo 0
    - server poté bude očekávat zprávu typu délky zprávy o 4 znacích s délkou