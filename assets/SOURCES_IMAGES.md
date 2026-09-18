# Sources des images — Manuel I : L'Héritage du Wuju

> Registre des illustrations utilisées ou prévues dans le manuel.

| Fichier local | Sujet | Origine | Identifiant | Artiste | Source | Type | Usage | Statut |
|---|---|---|---|---|---|---|---|---|
| `01-couverture-heritage-du-wuju.jpg` | Temple Wuju / Ionia | Projet | — | — | — | Original | Couverture | À créer |
| `03-ch1-maitre-yi-officiel.jpg` | Master Yi | Riot / League of Legends | Champion Master Yi | Riot Games | Page champion Riot | Officiel Riot | Ouverture chapitre I | À collecter |
| `04-jun-officiel-lor.jpg` | Jun, the Prodigy | Legends of Runeterra | 06IO011 | Kudos Productions | LoR / Riot | Officiel Riot | Portrait / chapitre II | À collecter |
| `06-ch2-jun-the-prodigy.jpg` | Jun, the Prodigy | Legends of Runeterra | 06IO011 | Kudos Productions | LoR / Riot | Officiel Riot | Ouverture chapitre II | À collecter |
| `09-ting-vastayan-disciple.jpg` | Ting / Vastayan Disciple | Legends of Runeterra | 06IO014 | Polar Engine | LoR / Riot | Officiel Riot | Disciple Wuju | À collecter |
| `10-disciple-de-doran.jpg` | Disciple of Doran | Legends of Runeterra | 06IO001 | Polar Engine | LoR / Riot | Officiel Riot | Doran / artisanat | À collecter |
| `11-ch3-kayn-officiel.jpg` | Kayn | Riot / League of Legends | Champion Kayn | Riot Games | Page champion Riot | Officiel Riot | Ouverture chapitre III | À collecter |
| `16-rhaast-detail.jpg` | Rhaast | Riot / League of Legends | Kayn / Rhaast | Riot Games | Page champion Riot / art officiel | Officiel Riot | Encadré Darkin | À collecter |
| `17-xolaani-officiel-lor.jpg` | Xolaani (forme Bloodletters) | Legends of Runeterra | 06SH004T2 | Kudos Productions | LoR Data Dragon / Riot | Officiel Riot | Révélation / annexes | À collecter |
| `17b-xolaani-bloodweaver.jpg` | Xolaani the Bloodweaver | Legends of Runeterra | 06MT035 | Aron Elekes | LoR Data Dragon / Riot | Officiel Riot | Annexes Darkin | À collecter |
| `18-wuju-style.jpg` | Wuju Style | Legends of Runeterra | 06IO013 | Kudos Productions | LoR / Riot | Officiel Riot | Annexes Wuju | À collecter |
| `08-carte-chutes-joueurs.jpg` | Chutes de Brume | Projet | — | — | Projet | Original | Carte joueurs | À finaliser |
| `08b-carte-chutes-mj.jpg` | Chutes de Brume | Projet | — | — | Projet | Original | Carte MJ | À finaliser |
| `12-temple-wuju-general-mj.jpg` | Temple Wuju | Projet | — | — | Projet | Original | Carte générale MJ | À finaliser |
| `12b-temple-wuju-general-joueurs.jpg` | Temple Wuju | Projet | — | — | Projet | Original | Carte générale joueurs | À finaliser |
| `13-temple-niveau-moins-1.jpg` | Temple principal | Projet | — | — | Projet | Original | Battle map | À finaliser |
| `14-temple-niveau-moins-2.jpg` | Dortoirs / cloître | Projet | — | — | Projet | Original | Battle map | À finaliser |
| `15-temple-niveau-moins-3.jpg` | Reliquaire | Projet | — | — | Projet | Original | Battle map | À finaliser |

## Règle

Ne jamais supprimer la provenance d'un visuel une fois qu'il est intégré au manuel.


---

## Source Riot recommandée — LoR Data Dragon

Riot fournit officiellement les illustrations complètes des cartes dans les bundles **Legends of Runeterra Data Dragon**.

Documentation :
`https://support-developer.riotgames.com/hc/en-us/articles/22698735834515-Legends-of-Runeterra`

Format direct utilisé par le projet :

`https://dd.b.pvp.net/latest/set6/en_us/img/cards/<CODE>-full.png`

Illustrations prioritaires :

| Sujet | Code LoR | Fichier complet Riot |
|---|---|---|
| Master Yi | 06IO008 | `06IO008-full.png` |
| Jun, the Prodigy | 06IO011 | `06IO011-full.png` |
| Ting / Vastayan Disciple | 06IO014 | `06IO014-full.png` |
| Disciple of Doran | 06IO001 | `06IO001-full.png` |
| Wuju Style | 06IO013 | `06IO013-full.png` |
| Mistfall | 06IO030 | `06IO030-full.png` |
| Momentous Choice | 06IO034 | `06IO034-full.png` |
| Utter Devastation | 06SI036 | `06SI036-full.png` |
| Kayn | 06RU005 | `06RU005-full.png` |
| Rhaast | 06RU005T2 | `06RU005T2-full.png` |
| Xolaani (forme issue des Bloodletters) | 06SH004T2 | `06SH004T2-full.png` |
| Xolaani the Bloodweaver | 06MT035 | `06MT035-full.png` |
| The Darkin Bloodletters | 06SH004 | `06SH004-full.png` |

Le script `scripts/fetch_riot_assets.py` automatise cette récupération et essaie également le bundle `set6cde` en secours.

### Dimensions

D'après la documentation Riot :

- illustrations de sorts : généralement **1024 × 1024** ;
- illustrations d'unités : généralement **2048 × 1024** ;
- les fichiers `*-full.png` ne contiennent ni texte ni cadre de carte.

### Important

Conserver les noms d'artistes dans ce registre lorsque l'information est connue, même si l'actif est récupéré directement depuis Riot.
