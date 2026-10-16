# Como obter os .mcaddon

Os packs binários estão versionados em Base64 em `releases_b64/`.

```bash
git clone https://github.com/tsddev016/minecraft-bedrock-mods.git
cd minecraft-bedrock-mods
python3 decode_releases.py
```

A pasta `releases/` terá:

- MedidorEnergia_v1.3.mcaddon
- PCGamer_v1.3.2.mcaddon
- GridCarvao_1.0.1.mcaddon
- CineOS_Mobile_1.1.mcaddon
- VozProximidade_BP_v1.0.3.mcpack
- Televisao_v1.0.mcaddon
- GuiaDosMods.mcaddon
- voz-minecraft-completo.zip
