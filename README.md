# Minecraft Bedrock Mods

Repositório oficial das **versões mais atualizadas** dos add-ons Bedrock.

**Repo:** https://github.com/tsddev016/minecraft-bedrock-mods

## Packs (versões finais)

| Mod | Arquivo | Versão |
|-----|---------|--------|
| Medidor de Energia | `MedidorEnergia_v1.3.mcaddon` | **1.3** |
| PC Gamer | `PCGamer_v1.3.2.mcaddon` | **1.3.2** |
| Rede Elétrica a Carvão | `GridCarvao_1.0.1.mcaddon` | **1.0.1** |
| CineOS Mobile | `CineOS_Mobile_1.1.mcaddon` | **1.1** |
| Voz por Proximidade | `VozProximidade_BP_v1.0.3.mcpack` | **1.0.3** |
| Televisão | `Televisao_v1.0.mcaddon` | **1.0** |
| Guia dos Mods | `GuiaDosMods.mcaddon` | **1.3** |
| Voz (Node completo) | `voz-minecraft-completo.zip` | — |

## Onde estão os .mcaddon

Os arquivos binários são grandes para o push automático de texto. Opções:

1. **GitHub Releases** (recomendado): faça upload dos `.mcaddon` em *Releases → Create a new release* (tag `v1.0`).
2. Veja `CHECKSUMS.md` para validar integridade (SHA256).
3. Scripts auxiliares: `decode_releases.py`, `join_and_extract.py`.

## Como instalar no Minecraft

1. Baixe o `.mcaddon` / `.mcpack`
2. Abra no Minecraft (duplo clique) ou coloque nas pastas de development packs
3. No mundo: ative **Behavior Pack** + **Resource Pack**
4. Ligue **trapaças** para `/scriptevent`

### Guia no jogo
```
/scriptevent guia:menu
/scriptevent guia:livro
```

## Não instalar (antigos)

- Medidor **1.2** → use **1.3**
- PC Gamer **1.0 / 1.1 / 1.2** → use **1.3.2**
- **InternetSimulada 1.0** → use **CineOS Mobile 1.1** (mesmo UUID)
- Grid sem **1.0.1** → use **1.0.1**

## Destaques das versões

- **PC 1.3.2:** tomada autoenergizada (sem redstone), montagem salva ao sair, sem spam no chat, monitor estilo Windows, PC com vidro/fans
- **Guia 1.3:** item Manual dos Mods ao entrar/morrer
- **Medidor 1.3:** lâmpadas + aparelhos externos (PC)
- **Grid 1.0.1:** usina a carvão → AT/BT → redstone

## Código

Pasta `source/` (scripts principais).
