# 🚀 Aurora Site Completo - Instruções

## ✨ O que está incluído:

✅ **index.html** - Site completo com:
   - Player de áudio fixo no canto inferior esquerdo
   - Legendas sincronizadas em tempo real (aparecem abaixo do player)
   - Sons interativos em TODOS os cliques
   - Sons especiais ao clicar em elementos 3D (partículas roxas)
   - Sons de hover ao passar o mouse

✅ **captions.vtt** - Legendas prontas baseadas em:
   - "FUTURE TECHNOLOGY"
   - "INNOVATION BEYOND BOUNDARIES"
   - Textos das suas imagens

## 📁 Arquivos que VOCÊ precisa adicionar:

### 1. Pasta audio/
- **scientific.mp3** - Áudio principal (narração científica de 30s-2min)

### 2. Pasta sounds/
- **click.mp3** - Som de clique (0.1-0.3s)
- **hover.mp3** - Som ao passar mouse (0.1-0.3s)
- **special.mp3** - Som para elementos 3D (0.2-0.3s)

## 🎵 Onde baixar sons GRÁTIS:

### Sons Interativos (curtos):
- https://freesound.org (pesquise: "ui click", "ui hover", "space sound")
- https://zapsplat.com/sound-effect-category/user-interface/
- https://mixkit.co/free-sound-effects/click/

### Áudio Científico:
- YouTube Audio Library (filtro: "sci-fi", "technology")
- https://www.bensound.com (categoria: futuristic)
- Grave sua própria narração científica

## 🚀 Como usar:

### Opção 0: Script automático `abrir_site.py`
1. Certifique-se de ter o Python 3 instalado.
2. No terminal, execute:
   ```bash
   python abrir_site.py
   ```
   *(Use `python3` no macOS/Linux, se necessário.)*
3. O navegador abrirá automaticamente em http://127.0.0.1:5500/index.html.
4. Pressione **CTRL+C** no terminal para encerrar o servidor quando terminar.

### Opção 1: VS Code Live Server (RECOMENDADO)
1. Abra a pasta no VS Code
2. Instale extensão "Live Server"
3. Clique direito em index.html → "Open with Live Server"
4. Acesse http://localhost:5500

### Opção 2: Python
```bash
cd aurora_site_completo
python -m http.server 8000
```
Acesse: http://localhost:8000

### Opção 3: Node.js
```bash
npx http-server
```

## 🎮 Funcionalidades:

### Sons Interativos:
- ✅ Clique em QUALQUER lugar: toca click.mp3
- ✅ Clique em elementos 3D (canvas/partículas): toca special.mp3
- ✅ Passar mouse em botões/links: toca hover.mp3

### Legendas:
- ✅ Aparecem automaticamente no player
- ✅ Sincronizadas com o áudio
- ✅ Design moderno com fundo transparente

## ⚙️ Personalizar:

### Ajustar volumes (no index.html):
- clickSounds.general.volume = 0.3 (30%)
- clickSounds.hover.volume = 0.2 (20%)
- clickSounds.special.volume = 0.5 (50%)

### Editar legendas (captions.vtt):
```
00:00.000 --> 00:05.000
Seu texto aqui
```

## ❗ IMPORTANTE:

- Não funciona abrindo index.html diretamente (use servidor local)
- Navegadores bloqueiam áudio sem interação do usuário (normal)
- Adicione seus arquivos MP3 nas pastas corretas
- Mantenha os nomes dos arquivos exatamente como indicado

## 📞 Problemas?

1. Sons não tocam → Adicione os arquivos MP3
2. Legendas não aparecem → Use servidor local (não abra direto)
3. Player não aparece → Verifique console do navegador (F12)

Divirta-se! 🎉
