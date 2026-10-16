# Minecraft Bedrock Mods

Repositório com as **versões mais atualizadas** dos add-ons Bedrock do projeto.

## Downloads

Os arquivos `.mcaddon` / `.mcpack` estão em `releases_b64/` (Base64).

Para gerar os arquivos de jogo:

```bash
python3 decode_releases.py
```

Isso cria a pasta `releases/` com os packs prontos para o Minecraft.

| Mod | Arquivo | Versão |
|-----|---------|--------|
| Medidor de Energia | `MedidorEnergia_v1.3.mcaddon` | 1.3 |
| PC Gamer | `PCGamer_v1.3.2.mcaddon` | 1.3.2 |
| Rede Elétrica a Carvão | `GridCarvao_1.0.1.mcaddon` | 1.0.1 |
| CineOS Mobile | `CineOS_Mobile_1.1.mcaddon` | 1.1 |
| Voz por Proximidade | `VozProximidade_BP_v1.0.3.mcpack` | 1.0.3 |
| Televisão | `Televisao_v1.0.mcaddon` | 1.0 |
| Guia dos Mods | `GuiaDosMods.mcaddon` | 1.3 |
| Voz (completo Node) | `voz-minecraft-completo.zip` | — |

### Como instalar
1. Decodifique os packs (`python3 decode_releases.py`) ou baixe os `.b64` e converta
2. Abra o `.mcaddon` no Minecraft
3. Ative Behavior + Resource no mundo
4. Trapaças ligadas para `/scriptevent`

### Guia no jogo
```
/scriptevent guia:menu
/scriptevent guia:livro
```

### Não instalar (antigos)
- Medidor 1.2 → use 1.3
- PC 1.0/1.1/1.2 → use 1.3.2
- InternetSimulada 1.0 → use CineOS 1.1
- Grid sem 1.0.1 → use 1.0.1

### Código-fonte
Pasta `source/` com scripts principais.
