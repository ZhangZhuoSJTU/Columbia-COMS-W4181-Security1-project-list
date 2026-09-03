# 💥 SIGSEGV Hacking: The COMS W4181 Course Project

The semester-long competition of **COMS W4181 Security I**, built on
[ProgramBench](https://github.com/facebookresearch/programbench): every student maintains a real
open-source program, plants a bug in it, and hunts for the bugs planted by everyone else.

## Rules

The competition runs in **three rounds**. In each round:

1. **Injection phase.** Each student selects one program from the project list below, injects a
   **crash-inducing bug**, and privately submits a proof-of-concept (PoC) input to the TAs to
   demonstrate the bug.
2. **Attack phase.** Students try to discover the bugs injected into other students' programs and
   submit PoCs to the TAs as proof of each discovery.

### Scoring

Per round, with placeholder weights $A$ (submission), $B$ (defense/attack), $C$ (first blood),
and $D$ (fresh-project bonus):

- **Submission score.** Submitting the modified program on time earns a base score of $A$. Each
  late day deducts $A/3$; at most **three late days** are allowed:

$$
S_{\mathrm{submit}} = A\left(1 - \frac{d}{3}\right), \qquad d \in \{0, 1, 2, 3\}
$$

  where $d$ is the number of late days.

- **Defense score.** Each student starts the round with a defense score of $B$. They keep the
  full $B$ if **no one** discovers their bug, and lose it otherwise:

$$
S_{\mathrm{defense}} = B \cdot \mathbb{1}\left[\text{your bug was not discovered}\right]
$$

- **Attack score.** For each bug, a total attack score of $B$ is divided equally among everyone
  who finds it — if $n_b$ students find bug $b$, each receives $B/n_b$. A student who discovers
  the set of bugs $\mathcal{B}$ earns:

$$
S_{\mathrm{attack}} = \sum_{b \in \mathcal{B}} \frac{B}{n_b}
$$

- **First blood.** The **first** student to discover each bug receives an additional bonus of
  $C$. With $f$ first-blood discoveries:

$$
S_{\mathrm{blood}} = C \cdot f
$$

- **Fresh-project bonus.** A student who selects a project that **no previous round has
  touched** (see the *Used in round* column below) earns an extra $D$:

$$
S_{\mathrm{fresh}} = D \cdot \mathbb{1}\left[\text{your project was untouched in all previous rounds}\right]
$$

**Round total:**

$$
S_{\mathrm{round}} = \underbrace{A\left(1 - \frac{d}{3}\right)}_{\text{submission}} + \underbrace{B \cdot \mathbb{1}\left[\text{bug not discovered}\right]}_{\text{defense}} + \underbrace{\sum_{b \in \mathcal{B}} \frac{B}{n_b}}_{\text{attack}} + \underbrace{C \cdot f}_{\text{first blood}} + \underbrace{D \cdot \mathbb{1}\left[\text{fresh project}\right]}_{\text{fresh bonus}}
$$

The final grade is the sum over the three rounds. The concrete values of $A$, $B$, $C$, $D$ will
be announced per round.

## Building and testing a project

Each prepared project ships two scripts at the repository root (requirements: the project's
toolchain — Go, Rust, or a C compiler — plus `python3` and `curl`):

- `./compile.sh` — compiles the current working tree (including any local changes you have made)
  into a binary named `./executable`.
- `./test.sh` — recompiles, then downloads (and caches) the ProgramBench test suites and runs all
  of them against your binary, printing a per-suite and total pass summary.

The intended workflow is simply: edit the code, run `./test.sh`, repeat.

## Project list

Each project links **directly to our forked repository**, reverted to the exact commit the
benchmark was built from, with `compile.sh` and `test.sh` already added at the root — clone the
fork and you are ready to build and test. *Tests (ProgramBench)* is the total number of
behavioral tests the benchmark ships for the project; *Tests kept* is the number we keep after
removing tests that ProgramBench flags as unreliable (N/A = project not yet prepared, fork link
may not exist yet). Each project must be validated by all three TAs before it can be selected.

**Ported so far: 7 / 198**

| Project | Commit | Tests (ProgramBench) | Tests kept | Used in round | Annie | SeungHyun | Madalina |
|---|---|---:|---:|:-:|:-:|:-:|:-:|
| [abishekvashok/cmatrix](https://github.com/ZhangZhuoSJTU/cmatrix) | `5c082c6` | 769 | N/A | — | ⬜ | ⬜ | ⬜ |
| [agourlay/zip-password-finder](https://github.com/ZhangZhuoSJTU/zip-password-finder) | `704700d` | 792 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ajeetdsouza/zoxide](https://github.com/ZhangZhuoSJTU/zoxide) | `67ca1bc` | 577 | N/A | — | ⬜ | ⬜ | ⬜ |
| [alecthomas/chroma](https://github.com/ZhangZhuoSJTU/chroma) | `8d04def` | 531 | N/A | — | ⬜ | ⬜ | ⬜ |
| [alexpovel/srgn](https://github.com/ZhangZhuoSJTU/srgn) | `89f943b` | 2080 | N/A | — | ⬜ | ⬜ | ⬜ |
| [altdesktop/i3-style](https://github.com/ZhangZhuoSJTU/i3-style) | `f93821b` | 750 | N/A | — | ⬜ | ⬜ | ⬜ |
| [AmmarAbouZor/tui-journal](https://github.com/ZhangZhuoSJTU/tui-journal) | `2b4540d` | 1839 | N/A | — | ⬜ | ⬜ | ⬜ |
| [anordal/shellharden](https://github.com/ZhangZhuoSJTU/shellharden) | `6a6ffd4` | 1292 | 1095 | — | ⬜ | ⬜ | ⬜ |
| [antonmedv/fx](https://github.com/ZhangZhuoSJTU/fx) | `86d0d34` | 3157 | N/A | — | ⬜ | ⬜ | ⬜ |
| [antonmedv/walk](https://github.com/ZhangZhuoSJTU/walk) | `bf802ef` | 786 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ariga/atlas](https://github.com/ZhangZhuoSJTU/atlas) | `6d81150` | 1732 | N/A | — | ⬜ | ⬜ | ⬜ |
| [arq5x/bedtools2](https://github.com/ZhangZhuoSJTU/bedtools2) | `dd57059` | 1093 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ArthurSonzogni/json-tui](https://github.com/ZhangZhuoSJTU/json-tui) | `17a22b6` | 894 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ast-grep/ast-grep](https://github.com/ZhangZhuoSJTU/ast-grep) | `dde0fe0` | 895 | N/A | — | ⬜ | ⬜ | ⬜ |
| [astaxie/bat](https://github.com/ZhangZhuoSJTU/bat-astaxie) | `17d1080` | 1462 | N/A | — | ⬜ | ⬜ | ⬜ |
| [astro/deadnix](https://github.com/ZhangZhuoSJTU/deadnix) | `d590041` | 709 | N/A | — | ⬜ | ⬜ | ⬜ |
| [axodotdev/oranda](https://github.com/ZhangZhuoSJTU/oranda) | `27d60c7` | 978 | N/A | — | ⬜ | ⬜ | ⬜ |
| [bellard/quickjs](https://github.com/ZhangZhuoSJTU/quickjs) | `d7ae12a` | 3044 | N/A | — | ⬜ | ⬜ | ⬜ |
| [bensadeh/tailspin](https://github.com/ZhangZhuoSJTU/tailspin) | `6278437` | 785 | N/A | — | ⬜ | ⬜ | ⬜ |
| [blacknon/hwatch](https://github.com/ZhangZhuoSJTU/hwatch) | `edfcb62` | 1321 | N/A | — | ⬜ | ⬜ | ⬜ |
| [BLAKE3-team/BLAKE3](https://github.com/ZhangZhuoSJTU/BLAKE3) | `15e83a5` | 687 | N/A | — | ⬜ | ⬜ | ⬜ |
| [bootandy/dust](https://github.com/ZhangZhuoSJTU/dust) | `62bf1e1` | 965 | N/A | — | ⬜ | ⬜ | ⬜ |
| [boyter/scc](https://github.com/ZhangZhuoSJTU/scc) | `515f91c` | 476 | N/A | — | ⬜ | ⬜ | ⬜ |
| [brocode/fblog](https://github.com/ZhangZhuoSJTU/fblog) | `3b54330` | 1127 | N/A | — | ⬜ | ⬜ | ⬜ |
| [BurntSushi/ripgrep](https://github.com/ZhangZhuoSJTU/ripgrep) | `3b7fd44` | 2538 | N/A | — | ⬜ | ⬜ | ⬜ |
| [BurntSushi/xsv](https://github.com/ZhangZhuoSJTU/xsv) | `f430466` | 1323 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Byron/dua-cli](https://github.com/ZhangZhuoSJTU/dua-cli) | `8570c15` | 1003 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Canop/broot](https://github.com/ZhangZhuoSJTU/broot) | `d6c798e` | 850 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Canop/rhit](https://github.com/ZhangZhuoSJTU/rhit) | `ae90bcb` | 1088 | N/A | — | ⬜ | ⬜ | ⬜ |
| [cheat/cheat](https://github.com/ZhangZhuoSJTU/cheat) | `b8098dc` | 307 | N/A | — | ⬜ | ⬜ | ⬜ |
| [chirlu/sox](https://github.com/ZhangZhuoSJTU/sox) | `42b3557` | 1260 | N/A | — | ⬜ | ⬜ | ⬜ |
| [chmln/handlr](https://github.com/ZhangZhuoSJTU/handlr) | `90e78ba` | 908 | N/A | — | ⬜ | ⬜ | ⬜ |
| [chmln/sd](https://github.com/ZhangZhuoSJTU/sd) | `87d1ba5` | 869 | N/A | — | ⬜ | ⬜ | ⬜ |
| [clog-tool/clog-cli](https://github.com/ZhangZhuoSJTU/clog-cli) | `7066cba` | 778 | N/A | — | ⬜ | ⬜ | ⬜ |
| [cmatsuoka/figlet](https://github.com/ZhangZhuoSJTU/figlet) | `202a0a8` | 1044 | N/A | — | ⬜ | ⬜ | ⬜ |
| [codesnap-rs/codesnap](https://github.com/ZhangZhuoSJTU/codesnap) | `f81e4f3` | 871 | N/A | — | ⬜ | ⬜ | ⬜ |
| [cordx56/rustowl](https://github.com/ZhangZhuoSJTU/rustowl) | `655bc5c` | 763 | N/A | — | ⬜ | ⬜ | ⬜ |
| [crowdagger/crowbook](https://github.com/ZhangZhuoSJTU/crowbook) | `ea214d7` | 887 | N/A | — | ⬜ | ⬜ | ⬜ |
| [cslarsen/jp2a](https://github.com/ZhangZhuoSJTU/jp2a) | `61d205f` | 714 | N/A | — | ⬜ | ⬜ | ⬜ |
| [cweill/gotests](https://github.com/ZhangZhuoSJTU/gotests) | `2a672c5` | 752 | N/A | — | ⬜ | ⬜ | ⬜ |
| [dalance/amber](https://github.com/ZhangZhuoSJTU/amber) | `69a0f52` | 785 | N/A | — | ⬜ | ⬜ | ⬜ |
| [dandavison/delta](https://github.com/ZhangZhuoSJTU/delta) | `acd758f` | 1188 | N/A | — | ⬜ | ⬜ | ⬜ |
| [danmar/cppcheck](https://github.com/ZhangZhuoSJTU/cppcheck) | `0a5b103` | 2550 | N/A | — | ⬜ | ⬜ | ⬜ |
| [direnv/direnv](https://github.com/ZhangZhuoSJTU/direnv) | `02040c7` | 986 | N/A | — | ⬜ | ⬜ | ⬜ |
| [doxygen/doxygen](https://github.com/ZhangZhuoSJTU/doxygen) | `966d98e` | 252 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Drew-Alleman/DataSurgeon](https://github.com/ZhangZhuoSJTU/DataSurgeon) | `d257cee` | 564 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ducaale/xh](https://github.com/ZhangZhuoSJTU/xh) | `4a6e44f` | 1266 | N/A | — | ⬜ | ⬜ | ⬜ |
| [duckdb/duckdb](https://github.com/ZhangZhuoSJTU/duckdb) | `bdb65ec` | 8958 | N/A | — | ⬜ | ⬜ | ⬜ |
| [dundee/gdu](https://github.com/ZhangZhuoSJTU/gdu) | `ede21d2` | 1553 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ecumene/rust-sloth](https://github.com/ZhangZhuoSJTU/rust-sloth) | `051c559` | 455 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ekzhang/bore](https://github.com/ZhangZhuoSJTU/bore) | `8e059cd` | 452 | N/A | — | ⬜ | ⬜ | ⬜ |
| [eliukblau/pixterm](https://github.com/ZhangZhuoSJTU/pixterm) | `1a93fd5` | 458 | 423 | — | ⬜ | ⬜ | ⬜ |
| [elkowar/pipr](https://github.com/ZhangZhuoSJTU/pipr) | `fae0b17` | 835 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Epistates/treemd](https://github.com/ZhangZhuoSJTU/treemd) | `825c6dd` | 1961 | N/A | — | ⬜ | ⬜ | ⬜ |
| [eradman/entr](https://github.com/ZhangZhuoSJTU/entr) | `8e2e8b4` | 685 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Esubaalew/run](https://github.com/ZhangZhuoSJTU/run) | `0fb9dec` | 1507 | N/A | — | ⬜ | ⬜ | ⬜ |
| [eudoxia0/hashcards](https://github.com/ZhangZhuoSJTU/hashcards) | `48aa136` | 1293 | N/A | — | ⬜ | ⬜ | ⬜ |
| [facebook/zstd](https://github.com/ZhangZhuoSJTU/zstd) | `1168da0` | 2372 | N/A | — | ⬜ | ⬜ | ⬜ |
| [facebookresearch/fastText](https://github.com/ZhangZhuoSJTU/fastText) | `1142dc4` | 352 | N/A | — | ⬜ | ⬜ | ⬜ |
| [FFmpeg/FFmpeg](https://github.com/ZhangZhuoSJTU/FFmpeg) | `360a402` | 4165 | N/A | — | ⬜ | ⬜ | ⬜ |
| [FiloSottile/age](https://github.com/ZhangZhuoSJTU/age) | `706dfc1` | 839 | N/A | — | ⬜ | ⬜ | ⬜ |
| [foriequal0/git-trim](https://github.com/ZhangZhuoSJTU/git-trim) | `07c2f50` | 726 | N/A | — | ⬜ | ⬜ | ⬜ |
| [gabotechs/dep-tree](https://github.com/ZhangZhuoSJTU/dep-tree) | `60a95a2` | 1428 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ggreer/the_silver_searcher](https://github.com/ZhangZhuoSJTU/the_silver_searcher) | `a61f178` | 1192 | N/A | — | ⬜ | ⬜ | ⬜ |
| [git-bahn/git-graph](https://github.com/ZhangZhuoSJTU/git-graph) | `87b4473` | 733 | N/A | — | ⬜ | ⬜ | ⬜ |
| [go-critic/go-critic](https://github.com/ZhangZhuoSJTU/go-critic) | `9aea378` | 925 | N/A | — | ⬜ | ⬜ | ⬜ |
| [google/brotli](https://github.com/ZhangZhuoSJTU/brotli) | `b3dc9cc` | 606 | N/A | — | ⬜ | ⬜ | ⬜ |
| [gromacs/gromacs](https://github.com/ZhangZhuoSJTU/gromacs) | `665ea4c` | 1382 | N/A | — | ⬜ | ⬜ | ⬜ |
| [guumaster/hostctl](https://github.com/ZhangZhuoSJTU/hostctl) | `d6d9699` | 1385 | N/A | — | ⬜ | ⬜ | ⬜ |
| [hairyhenderson/gomplate](https://github.com/ZhangZhuoSJTU/gomplate) | `05eb3aa` | 3538 | N/A | — | ⬜ | ⬜ | ⬜ |
| [HaliteChallenge/Halite](https://github.com/ZhangZhuoSJTU/Halite) | `822cfb6` | 391 | N/A | — | ⬜ | ⬜ | ⬜ |
| [hatoo/oha](https://github.com/ZhangZhuoSJTU/oha) | `8dc6349` | 1095 | N/A | — | ⬜ | ⬜ | ⬜ |
| [hooklift/gowsdl](https://github.com/ZhangZhuoSJTU/gowsdl) | `2a06cec` | 419 | N/A | — | ⬜ | ⬜ | ⬜ |
| [hpjansson/chafa](https://github.com/ZhangZhuoSJTU/chafa) | `dd4d4c1` | 2775 | N/A | — | ⬜ | ⬜ | ⬜ |
| [htop-dev/htop](https://github.com/ZhangZhuoSJTU/htop) | `523600b` | 1200 | N/A | — | ⬜ | ⬜ | ⬜ |
| [hush-shell/hush](https://github.com/ZhangZhuoSJTU/hush) | `560c33a` | 1298 | N/A | — | ⬜ | ⬜ | ⬜ |
| [incu6us/goimports-reviser](https://github.com/ZhangZhuoSJTU/goimports-reviser) | `81bd549` | 597 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ip7z/7zip](https://github.com/ZhangZhuoSJTU/7zip) | `839151e` | 1085 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ismaelgv/rnr](https://github.com/ZhangZhuoSJTU/rnr) | `fc0733b` | 742 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Isona/dirble](https://github.com/ZhangZhuoSJTU/dirble) | `e2dea9f` | 1108 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ivanceras/svgbob](https://github.com/ZhangZhuoSJTU/svgbob) | `6d00ad9` | 474 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jarun/nnn](https://github.com/ZhangZhuoSJTU/nnn) | `cb2c535` | 1796 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jesseduffield/lazygit](https://github.com/ZhangZhuoSJTU/lazygit) | `1d0db51` | 1167 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jhspetersson/fselect](https://github.com/ZhangZhuoSJTU/fselect) | `c3559ca` | 3435 | N/A | — | ⬜ | ⬜ | ⬜ |
| [JohannesKaufmann/html-to-markdown](https://github.com/ZhangZhuoSJTU/html-to-markdown) | `3006818` | 974 | N/A | — | ⬜ | ⬜ | ⬜ |
| [johnkerl/miller](https://github.com/ZhangZhuoSJTU/miller) | `8d85b46` | 16070 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jonas/tig](https://github.com/ZhangZhuoSJTU/tig) | `8334123` | 2239 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jqlang/jq](https://github.com/ZhangZhuoSJTU/jq) | `b33a763` | 6796 | N/A | — | ⬜ | ⬜ | ⬜ |
| [jrnxf/thokr](https://github.com/ZhangZhuoSJTU/thokr) | `09375ef` | 507 | N/A | — | ⬜ | ⬜ | ⬜ |
| [junegunn/fzf](https://github.com/ZhangZhuoSJTU/fzf) | `b56d614` | 2164 | N/A | — | ⬜ | ⬜ | ⬜ |
| [kaushiksrini/parqeye](https://github.com/ZhangZhuoSJTU/parqeye) | `8072121` | 564 | N/A | — | ⬜ | ⬜ | ⬜ |
| [kisielk/errcheck](https://github.com/ZhangZhuoSJTU/errcheck) | `dacab89` | 532 | 340 | — | ⬜ | ⬜ | ⬜ |
| [konradsz/igrep](https://github.com/ZhangZhuoSJTU/igrep) | `aa75630` | 728 | N/A | — | ⬜ | ⬜ | ⬜ |
| [KSXGitHub/parallel-disk-usage](https://github.com/ZhangZhuoSJTU/parallel-disk-usage) | `96978ed` | 630 | N/A | — | ⬜ | ⬜ | ⬜ |
| [kyoh86/richgo](https://github.com/ZhangZhuoSJTU/richgo) | `313114f` | 787 | N/A | — | ⬜ | ⬜ | ⬜ |
| [kyoheiu/felix](https://github.com/ZhangZhuoSJTU/felix) | `95df390` | 979 | N/A | — | ⬜ | ⬜ | ⬜ |
| [lfos/calcurse](https://github.com/ZhangZhuoSJTU/calcurse) | `49180d5` | 1994 | N/A | — | ⬜ | ⬜ | ⬜ |
| [lh3/seqtk](https://github.com/ZhangZhuoSJTU/seqtk) | `94e7070` | 440 | N/A | — | ⬜ | ⬜ | ⬜ |
| [lua/lua](https://github.com/ZhangZhuoSJTU/lua) | `c6b4848` | 1387 | N/A | — | ⬜ | ⬜ | ⬜ |
| [LuaJIT/LuaJIT](https://github.com/ZhangZhuoSJTU/LuaJIT) | `a553b3d` | 3183 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Lymphatus/caesium-clt](https://github.com/ZhangZhuoSJTU/caesium-clt) | `a529b2e` | 616 | N/A | — | ⬜ | ⬜ | ⬜ |
| [lz4/lz4](https://github.com/ZhangZhuoSJTU/lz4) | `1519f46` | 1829 | N/A | — | ⬜ | ⬜ | ⬜ |
| [madler/pigz](https://github.com/ZhangZhuoSJTU/pigz) | `fe4894f` | 938 | N/A | — | ⬜ | ⬜ | ⬜ |
| [mfridman/tparse](https://github.com/ZhangZhuoSJTU/tparse) | `2416b4b` | 556 | N/A | — | ⬜ | ⬜ | ⬜ |
| [mgdm/htmlq](https://github.com/ZhangZhuoSJTU/htmlq) | `6e31bc8` | 2058 | 1455 | — | ⬜ | ⬜ | ⬜ |
| [mgechev/revive](https://github.com/ZhangZhuoSJTU/revive) | `201451e` | 886 | N/A | — | ⬜ | ⬜ | ⬜ |
| [mibk/dupl](https://github.com/ZhangZhuoSJTU/dupl) | `1bf052b` | 450 | 370 | — | ⬜ | ⬜ | ⬜ |
| [mikefarah/yq](https://github.com/ZhangZhuoSJTU/yq) | `602586d` | 2046 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Miserlou/Loop](https://github.com/ZhangZhuoSJTU/Loop) | `209927c` | 778 | N/A | — | ⬜ | ⬜ | ⬜ |
| [mkj/dropbear](https://github.com/ZhangZhuoSJTU/dropbear) | `75f699b` | 1075 | N/A | — | ⬜ | ⬜ | ⬜ |
| [mookid/diffr](https://github.com/ZhangZhuoSJTU/diffr) | `2152742` | 782 | N/A | — | ⬜ | ⬜ | ⬜ |
| [multiprocessio/dsq](https://github.com/ZhangZhuoSJTU/dsq) | `c3ae0ba` | 766 | N/A | — | ⬜ | ⬜ | ⬜ |
| [nachoparker/dutree](https://github.com/ZhangZhuoSJTU/dutree) | `44e877d` | 957 | N/A | — | ⬜ | ⬜ | ⬜ |
| [naggie/dstask](https://github.com/ZhangZhuoSJTU/dstask) | `ff57396` | 1589 | N/A | — | ⬜ | ⬜ | ⬜ |
| [NikolaDucak/caps-log](https://github.com/ZhangZhuoSJTU/caps-log) | `2cf2d1e` | 1232 | N/A | — | ⬜ | ⬜ | ⬜ |
| [nikolassv/bartib](https://github.com/ZhangZhuoSJTU/bartib) | `6b9b5ce` | 929 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ninja-build/ninja](https://github.com/ZhangZhuoSJTU/ninja) | `cc60300` | 1905 | N/A | — | ⬜ | ⬜ | ⬜ |
| [noborus/ov](https://github.com/ZhangZhuoSJTU/ov) | `b96c2ba` | 2447 | N/A | — | ⬜ | ⬜ | ⬜ |
| [noborus/trdsql](https://github.com/ZhangZhuoSJTU/trdsql) | `d8c5ff6` | 1403 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Nukesor/pueue](https://github.com/ZhangZhuoSJTU/pueue) | `8b9d6fe` | 1223 | N/A | — | ⬜ | ⬜ | ⬜ |
| [nuta/nsh](https://github.com/ZhangZhuoSJTU/nsh) | `bdd0702` | 2289 | N/A | — | ⬜ | ⬜ | ⬜ |
| [o2sh/onefetch](https://github.com/ZhangZhuoSJTU/onefetch) | `e5958ce` | 1214 | N/A | — | ⬜ | ⬜ | ⬜ |
| [ogham/dog](https://github.com/ZhangZhuoSJTU/dog) | `721440b` | 1722 | N/A | — | ⬜ | ⬜ | ⬜ |
| [oppiliappan/eva](https://github.com/ZhangZhuoSJTU/eva) | `41ae245` | 963 | N/A | — | ⬜ | ⬜ | ⬜ |
| [oppiliappan/statix](https://github.com/ZhangZhuoSJTU/statix) | `e9df54c` | 983 | N/A | — | ⬜ | ⬜ | ⬜ |
| [orf/gping](https://github.com/ZhangZhuoSJTU/gping) | `26eb5b9` | 655 | N/A | — | ⬜ | ⬜ | ⬜ |
| [OSGeo/gdal](https://github.com/ZhangZhuoSJTU/gdal) | `0847f12` | 1319 | N/A | — | ⬜ | ⬜ | ⬜ |
| [OSGeo/PROJ](https://github.com/ZhangZhuoSJTU/PROJ) | `75d455c` | 7160 | N/A | — | ⬜ | ⬜ | ⬜ |
| [paradigmxyz/solar](https://github.com/ZhangZhuoSJTU/solar) | `5190d0e` | 2528 | N/A | — | ⬜ | ⬜ | ⬜ |
| [parcel-bundler/lightningcss](https://github.com/ZhangZhuoSJTU/lightningcss) | `aa2ed1e` | 3155 | N/A | — | ⬜ | ⬜ | ⬜ |
| [peco/peco](https://github.com/ZhangZhuoSJTU/peco) | `4e58dad` | 1715 | N/A | — | ⬜ | ⬜ | ⬜ |
| [pemistahl/grex](https://github.com/ZhangZhuoSJTU/grex) | `fa3e8ed` | 1518 | N/A | — | ⬜ | ⬜ | ⬜ |
| [php/php-src](https://github.com/ZhangZhuoSJTU/php-src) | `c891263` | 20530 | N/A | — | ⬜ | ⬜ | ⬜ |
| [pier-cli/pier](https://github.com/ZhangZhuoSJTU/pier) | `5e1bde9` | 779 | N/A | — | ⬜ | ⬜ | ⬜ |
| [pls-rs/pls](https://github.com/ZhangZhuoSJTU/pls) | `4e1ae50` | 354 | N/A | — | ⬜ | ⬜ | ⬜ |
| [psampaz/go-mod-outdated](https://github.com/ZhangZhuoSJTU/go-mod-outdated) | `bb79367` | 342 | 284 | — | ⬜ | ⬜ | ⬜ |
| [quinn-rs/quinn](https://github.com/ZhangZhuoSJTU/quinn) | `bb359cc` | 620 | N/A | — | ⬜ | ⬜ | ⬜ |
| [raviqqe/muffet](https://github.com/ZhangZhuoSJTU/muffet) | `a882908` | 432 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rbakbashev/elfcat](https://github.com/ZhangZhuoSJTU/elfcat) | `52f8cc7` | 646 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rcoh/angle-grinder](https://github.com/ZhangZhuoSJTU/angle-grinder) | `9c2fc88` | 1143 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rhysd/kiro-editor](https://github.com/ZhangZhuoSJTU/kiro-editor) | `4157485` | 770 | N/A | — | ⬜ | ⬜ | ⬜ |
| [riquito/tuc](https://github.com/ZhangZhuoSJTU/tuc) | `16fb471` | 1249 | N/A | — | ⬜ | ⬜ | ⬜ |
| [robertdavidgraham/masscan](https://github.com/ZhangZhuoSJTU/masscan) | `b99d433` | 3357 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rochacbruno/marmite](https://github.com/ZhangZhuoSJTU/marmite) | `7d4bc2d` | 853 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rs/curlie](https://github.com/ZhangZhuoSJTU/curlie) | `5dfcbb1` | 741 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rs/jplot](https://github.com/ZhangZhuoSJTU/jplot) | `2a54bcc` | 722 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rust-embedded/svd2rust](https://github.com/ZhangZhuoSJTU/svd2rust) | `1760b5e` | 985 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rust-ethereum/ethabi](https://github.com/ZhangZhuoSJTU/ethabi) | `b1710ad` | 1053 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rust-lang/mdBook](https://github.com/ZhangZhuoSJTU/mdBook) | `37273ba` | 1326 | N/A | — | ⬜ | ⬜ | ⬜ |
| [rvben/rumdl](https://github.com/ZhangZhuoSJTU/rumdl) | `2d75c4d` | 4781 | N/A | — | ⬜ | ⬜ | ⬜ |
| [samtools/samtools](https://github.com/ZhangZhuoSJTU/samtools) | `aa823b5` | 1819 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sayanarijit/xplr](https://github.com/ZhangZhuoSJTU/xplr) | `1751065` | 939 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sclevine/yj](https://github.com/ZhangZhuoSJTU/yj) | `8016400` | 825 | 768 | — | ⬜ | ⬜ | ⬜ |
| [segmentio/chamber](https://github.com/ZhangZhuoSJTU/chamber) | `5f93f5f` | 3104 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sharkdp/bat](https://github.com/ZhangZhuoSJTU/bat-sharkdp) | `f822bd0` | 986 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sharkdp/fd](https://github.com/ZhangZhuoSJTU/fd) | `40d8eb3` | 1405 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sharkdp/hexyl](https://github.com/ZhangZhuoSJTU/hexyl) | `2e26437` | 974 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sharkdp/hyperfine](https://github.com/ZhangZhuoSJTU/hyperfine) | `327d5f4` | 298 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sharkdp/pastel](https://github.com/ZhangZhuoSJTU/pastel) | `b60e899` | 1256 | N/A | — | ⬜ | ⬜ | ⬜ |
| [shashwatah/jot](https://github.com/ZhangZhuoSJTU/jot) | `a92aad8` | 846 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sheepla/pingu](https://github.com/ZhangZhuoSJTU/pingu) | `926d475` | 419 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sibprogrammer/xq](https://github.com/ZhangZhuoSJTU/xq) | `b89f681` | 879 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sigoden/argc](https://github.com/ZhangZhuoSJTU/argc) | `04a08f1` | 1410 | N/A | — | ⬜ | ⬜ | ⬜ |
| [simeg/eureka](https://github.com/ZhangZhuoSJTU/eureka) | `df3796c` | 400 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sirwart/ripsecrets](https://github.com/ZhangZhuoSJTU/ripsecrets) | `34c9e03` | 937 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sitkevij/hex](https://github.com/ZhangZhuoSJTU/hex) | `61ae69b` | 877 | N/A | — | ⬜ | ⬜ | ⬜ |
| [skeema/skeema](https://github.com/ZhangZhuoSJTU/skeema) | `6a76243` | 3807 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sqlite/sqlite](https://github.com/ZhangZhuoSJTU/sqlite) | `839433d` | 16801 | N/A | — | ⬜ | ⬜ | ⬜ |
| [sstadick/hck](https://github.com/ZhangZhuoSJTU/hck) | `b66c751` | 884 | N/A | — | ⬜ | ⬜ | ⬜ |
| [stacked-git/stgit](https://github.com/ZhangZhuoSJTU/stgit) | `430027d` | 2340 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Stranger6667/jsonschema](https://github.com/ZhangZhuoSJTU/jsonschema) | `d52e881` | 3006 | N/A | — | ⬜ | ⬜ | ⬜ |
| [svenstaro/genact](https://github.com/ZhangZhuoSJTU/genact) | `16f96e3` | 237 | N/A | — | ⬜ | ⬜ | ⬜ |
| [svenstaro/miniserve](https://github.com/ZhangZhuoSJTU/miniserve) | `8449e8b` | 440 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tarka/xcp](https://github.com/ZhangZhuoSJTU/xcp) | `5e5b448` | 1236 | N/A | — | ⬜ | ⬜ | ⬜ |
| [TheZoraiz/ascii-image-converter](https://github.com/ZhangZhuoSJTU/ascii-image-converter) | `d05a757` | 488 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tinycc/tinycc](https://github.com/ZhangZhuoSJTU/tinycc) | `9b8765d` | 2062 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tomarrell/wrapcheck](https://github.com/ZhangZhuoSJTU/wrapcheck) | `c058da1` | 669 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tomnomnom/gron](https://github.com/ZhangZhuoSJTU/gron) | `88a6234` | 233 | N/A | — | ⬜ | ⬜ | ⬜ |
| [trasta298/keifu](https://github.com/ZhangZhuoSJTU/keifu) | `3331426` | 413 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tree-sitter/tree-sitter](https://github.com/ZhangZhuoSJTU/tree-sitter) | `5e23cca` | 1888 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tstack/lnav](https://github.com/ZhangZhuoSJTU/lnav) | `ee34494` | 1172 | N/A | — | ⬜ | ⬜ | ⬜ |
| [tukaani-project/xz](https://github.com/ZhangZhuoSJTU/xz) | `1007bf0` | 2036 | N/A | — | ⬜ | ⬜ | ⬜ |
| [typst/typst](https://github.com/ZhangZhuoSJTU/typst) | `88356d0` | 1789 | N/A | — | ⬜ | ⬜ | ⬜ |
| [unhappychoice/gittype](https://github.com/ZhangZhuoSJTU/gittype) | `34b72d0` | 932 | N/A | — | ⬜ | ⬜ | ⬜ |
| [universal-ctags/ctags](https://github.com/ZhangZhuoSJTU/ctags) | `243595e` | 2579 | N/A | — | ⬜ | ⬜ | ⬜ |
| [wfxr/code-minimap](https://github.com/ZhangZhuoSJTU/code-minimap) | `0ddeea5` | 370 | N/A | — | ⬜ | ⬜ | ⬜ |
| [wfxr/csview](https://github.com/ZhangZhuoSJTU/csview) | `8ac4de0` | 348 | N/A | — | ⬜ | ⬜ | ⬜ |
| [WGUNDERWOOD/tex-fmt](https://github.com/ZhangZhuoSJTU/tex-fmt) | `3f1aef6` | 495 | N/A | — | ⬜ | ⬜ | ⬜ |
| [wintermute-cell/ngrrram](https://github.com/ZhangZhuoSJTU/ngrrram) | `8ea13c3` | 332 | N/A | — | ⬜ | ⬜ | ⬜ |
| [XAMPPRocky/tokei](https://github.com/ZhangZhuoSJTU/tokei) | `505d648` | 760 | N/A | — | ⬜ | ⬜ | ⬜ |
| [xorg62/tty-clock](https://github.com/ZhangZhuoSJTU/tty-clock) | `f2f847c` | 319 | N/A | — | ⬜ | ⬜ | ⬜ |
| [Y2Z/monolith](https://github.com/ZhangZhuoSJTU/monolith) | `8702e66` | 777 | N/A | — | ⬜ | ⬜ | ⬜ |
| [yaa110/nomino](https://github.com/ZhangZhuoSJTU/nomino) | `f892499` | 338 | N/A | — | ⬜ | ⬜ | ⬜ |
| [yassinebridi/serpl](https://github.com/ZhangZhuoSJTU/serpl) | `c48a9d7` | 536 | N/A | — | ⬜ | ⬜ | ⬜ |
| [yoav-lavi/melody](https://github.com/ZhangZhuoSJTU/melody) | `f4af9b4` | 1438 | N/A | — | ⬜ | ⬜ | ⬜ |
| [YS-L/flamelens](https://github.com/ZhangZhuoSJTU/flamelens) | `0b4dc33` | 311 | N/A | — | ⬜ | ⬜ | ⬜ |
| [zevv/duc](https://github.com/ZhangZhuoSJTU/duc) | `a58fa4e` | 1246 | N/A | — | ⬜ | ⬜ | ⬜ |
| [zk-org/zk](https://github.com/ZhangZhuoSJTU/zk) | `10d93d5` | 1473 | N/A | — | ⬜ | ⬜ | ⬜ |
