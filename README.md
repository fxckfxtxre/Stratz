# Stratz
### Installation
```bash
pip install stratz
```

### Example
```python
import stratz
from stratz.lang import code_English


def main():
    api = stratz.Api(lang=code_English, token=<YOUR_BEARER_TOKEN>)

    player = api.get_player(91064780) #return player
    match = api.get_match(6279293344) #return match details
    hero = api.get_hero_by_name("npc_dota_hero_marci") #return hero Marci
    item = api.get_item_by_name("item_blink") #return item Blink
    

if __name__ == "__main__":
    main() 
```

---
https://docs.stratz.com/index.html
