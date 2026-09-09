# 💥 SIGSEGV Hacking: The COMS W4181 Course Project

The semester-long competition of **COMS W4181 Security I**, built on
[ProgramBench](https://github.com/facebookresearch/programbench): every student maintains a real
open-source program, plants a bug in it, and hunts for the bugs planted by everyone else.

## Rules

The full rules, the submission workflow and the scoring live on the
[course competition page](https://zzhang.xyz/teaching/security1-fall26/competition.html).
This is the same thing in short.

The competition runs in **two rounds**. In each round:

1. **Preparation phase.** Each student selects one program from the project list below, injects a
   **crash-inducing bug**, and privately submits a proof-of-concept (PoC) script to the TAs. The
   modified program must still build with `./compile.sh` and pass `./test.sh`.
2. **Attack phase.** Students try to discover the bugs injected into other students' programs and
   submit PoCs to the TAs as proof of each discovery.

Round 2 preparation officially opens when the Round 1 attack phase ends, but nothing stops you
from picking your Round 2 program and studying it earlier.

### Submitting

- **Register first.** By the end of the second week, email the TAs (CC the instructor) your UNI,
  your GitHub handle, and a competition password. The password is shared with nobody but the TAs
  and the instructor; every PoC you submit is a zip locked with it.
- **Your injected bug.** Fork our fork of the program (linked from the table below), inject the bug
  on a branch, and open a pull request against our fork titled `<UNI>-Round<N>` (for example
  `zz3474-Round1`). Attach `poc.sh` as a **password-protected zip** to the pull request
  description, then email the pull request link to the TAs, CC the instructor. The time the pull
  request was opened is your submission time; the email just tells the TAs where to look.
- **An attack.** Reproduce the crash on the target pull request's branch, name your script
  `<victim UNI>-<attacker UNI>-poc.sh` (the victim's UNI is in the pull request title), and upload
  it to that round's attack assignment on CourseWorks. No zip, no email, and nothing on GitHub:
  the CourseWorks timestamp is your discovery time and decides first blood.
- **The system clock is the time.** Submission time is when the pull request was opened on GitHub.
  Discovery time is when the PoC landed on CourseWorks. Never the emails.
- **A hint for defenders.** Everyone can run `diff` on your pull request, and a three-line change is
  found in minutes. Make the diff bigger than the bug: refactor around it, add semantically
  equivalent changes, touch several files. Obfuscating the diff is allowed; changing the build or
  test scripts is not. Do that and you are disqualified for the round: zero points, attack score
  included.
- **Leaderboard.** A leaderboard goes up once the competition starts. It is refreshed every week or
  two, except that a hacked challenge shows up right away.

### Scoring

Per round, with weights $A$ (submission), $B$ (defense/attack), $C$ (first blood), and $D$
(fresh-project bonus):

- **Submission score.** Submitting the modified program on time earns a base score of $A$. Each
  late day deducts $A/3$; at most **two late days** are allowed. After that the pull request does
  not count at all, for submission or defense, though you can still earn attack score that round:

$$
S_{\mathrm{submit}} = A\left(1 - \frac{d}{3}\right), \qquad d \in \{0, 1, 2\}
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

- **First blood.** The first **three** students to discover each bug receive a bonus of $C$,
  $0.8\,C$ and $0.6\,C$ respectively, in the order of their CourseWorks submissions:

$$
S_{\mathrm{blood}} = \sum_{b \in \mathcal{B}} c_b, \qquad c_b \in \{C,\; 0.8\,C,\; 0.6\,C,\; 0\} \text{ by your discovery rank on } b
$$

- **Fresh-project bonus.** The **first** student to open a valid pull request on a project that
  **no previous round has touched** (see the *Used in round* column below) earns an extra $D$.
  Only that student; later submissions on the same project do not. In Round 1 every project is
  fresh.

$$
S_{\mathrm{fresh}} = D \cdot \mathbb{1}\left[\text{yours was the first valid PR on a fresh project}\right]
$$

**Round total:**

$$
S_{\mathrm{round}} = \underbrace{A\left(1 - \frac{d}{3}\right)}_{\text{submission}} + \underbrace{B \cdot \mathbb{1}\left[\text{bug not discovered}\right]}_{\text{defense}} + \underbrace{\sum_{b \in \mathcal{B}} \frac{B}{n_b}}_{\text{attack}} + \underbrace{\sum_{b \in \mathcal{B}} c_b}_{\text{first blood}} + \underbrace{D \cdot \mathbb{1}\left[\text{first PR on a fresh project}\right]}_{\text{fresh bonus}}
$$

**Course grade.** The sum of your two round totals is curved before it goes into the course
grade: after the curve, the class median sits at 85% of the competition points. The curved score
is 40% of the course. The concrete values of $A$, $B$, $C$, $D$ will be announced per round.
will be announced per round.

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
may not exist yet). Each project must be validated by the TAs (the checkbox column) before it can be selected.
A per-project record of every dropped test and the reason it was dropped lives in
[docs/dropped-tests.md](docs/dropped-tests.md).

| Project | Commit | Tests (ProgramBench) | Tests kept | Used in round | TA checked |
|---|---|---:|---:|:-:|:-:|
| [abishekvashok/cmatrix](https://github.com/ZhangZhuoSJTU/cmatrix) | `5c082c6` | 769 | 491 | — | ⬜ |
| [agourlay/zip-password-finder](https://github.com/ZhangZhuoSJTU/zip-password-finder) | `704700d` | 792 | 680 | — | ⬜ |
| [ajeetdsouza/zoxide](https://github.com/ZhangZhuoSJTU/zoxide) | `67ca1bc` | 577 | 530 | — | ⬜ |
| [alecthomas/chroma](https://github.com/ZhangZhuoSJTU/chroma) | `8d04def` | 531 | 503 | — | ⬜ |
| [alexpovel/srgn](https://github.com/ZhangZhuoSJTU/srgn) | `89f943b` | 2080 | 1852 | — | ⬜ |
| [altdesktop/i3-style](https://github.com/ZhangZhuoSJTU/i3-style) | `f93821b` | 750 | 539 | — | ⬜ |
| [anordal/shellharden](https://github.com/ZhangZhuoSJTU/shellharden) | `6a6ffd4` | 1292 | 1095 | — | ⬜ |
| [antonmedv/fx](https://github.com/ZhangZhuoSJTU/fx) | `86d0d34` | 3157 | 2044 | — | ⬜ |
| [antonmedv/walk](https://github.com/ZhangZhuoSJTU/walk) | `bf802ef` | 786 | 404 | — | ⬜ |
| [ariga/atlas](https://github.com/ZhangZhuoSJTU/atlas) | `6d81150` | 1732 | 1312 | — | ⬜ |
| [arq5x/bedtools2](https://github.com/ZhangZhuoSJTU/bedtools2) | `dd57059` | 1093 | 1051 | — | ⬜ |
| [ArthurSonzogni/json-tui](https://github.com/ZhangZhuoSJTU/json-tui) | `17a22b6` | 894 | 715 | — | ⬜ |
| [ast-grep/ast-grep](https://github.com/ZhangZhuoSJTU/ast-grep) | `dde0fe0` | 895 | 830 | — | ⬜ |
| [astaxie/bat](https://github.com/ZhangZhuoSJTU/bat-astaxie) | `17d1080` | 1462 | 1062 | — | ⬜ |
| [astro/deadnix](https://github.com/ZhangZhuoSJTU/deadnix) | `d590041` | 709 | 602 | — | ⬜ |
| [axodotdev/oranda](https://github.com/ZhangZhuoSJTU/oranda) | `27d60c7` | 978 | 766 | — | ⬜ |
| [bellard/quickjs](https://github.com/ZhangZhuoSJTU/quickjs) | `d7ae12a` | 3044 | 3010 | — | ⬜ |
| [bensadeh/tailspin](https://github.com/ZhangZhuoSJTU/tailspin) | `6278437` | 785 | 611 | — | ⬜ |
| [blacknon/hwatch](https://github.com/ZhangZhuoSJTU/hwatch) | `edfcb62` | 1321 | 982 | — | ⬜ |
| [BLAKE3-team/BLAKE3](https://github.com/ZhangZhuoSJTU/BLAKE3) | `15e83a5` | 687 | 645 | — | ⬜ |
| [bootandy/dust](https://github.com/ZhangZhuoSJTU/dust) | `62bf1e1` | 965 | 545 | — | ⬜ |
| [boyter/scc](https://github.com/ZhangZhuoSJTU/scc) | `515f91c` | 476 | 457 | — | ⬜ |
| [brocode/fblog](https://github.com/ZhangZhuoSJTU/fblog) | `3b54330` | 1127 | 976 | — | ⬜ |
| [BurntSushi/ripgrep](https://github.com/ZhangZhuoSJTU/ripgrep) | `3b7fd44` | 2538 | 1981 | — | ⬜ |
| [BurntSushi/xsv](https://github.com/ZhangZhuoSJTU/xsv) | `f430466` | 1323 | 1181 | — | ⬜ |
| [Byron/dua-cli](https://github.com/ZhangZhuoSJTU/dua-cli) | `8570c15` | 1003 | 668 | — | ⬜ |
| [Canop/rhit](https://github.com/ZhangZhuoSJTU/rhit) | `ae90bcb` | 1088 | 813 | — | ⬜ |
| [cheat/cheat](https://github.com/ZhangZhuoSJTU/cheat) | `b8098dc` | 307 | 290 | — | ⬜ |
| [chirlu/sox](https://github.com/ZhangZhuoSJTU/sox) | `42b3557` | 1260 | 1194 | — | ⬜ |
| [chmln/handlr](https://github.com/ZhangZhuoSJTU/handlr) | `90e78ba` | 908 | 667 | — | ⬜ |
| [chmln/sd](https://github.com/ZhangZhuoSJTU/sd) | `87d1ba5` | 869 | 808 | — | ⬜ |
| [clog-tool/clog-cli](https://github.com/ZhangZhuoSJTU/clog-cli) | `7066cba` | 778 | 575 | — | ⬜ |
| [cmatsuoka/figlet](https://github.com/ZhangZhuoSJTU/figlet) | `202a0a8` | 1044 | 836 | — | ⬜ |
| [codesnap-rs/codesnap](https://github.com/ZhangZhuoSJTU/codesnap) | `f81e4f3` | 871 | 571 | — | ⬜ |
| [cordx56/rustowl](https://github.com/ZhangZhuoSJTU/rustowl) | `655bc5c` | 763 | 572 | — | ⬜ |
| [crowdagger/crowbook](https://github.com/ZhangZhuoSJTU/crowbook) | `ea214d7` | 887 | 807 | — | ⬜ |
| [cslarsen/jp2a](https://github.com/ZhangZhuoSJTU/jp2a) | `61d205f` | 714 | 628 | — | ⬜ |
| [cweill/gotests](https://github.com/ZhangZhuoSJTU/gotests) | `2a672c5` | 752 | 603 | — | ⬜ |
| [dandavison/delta](https://github.com/ZhangZhuoSJTU/delta) | `acd758f` | 1188 | 907 | — | ⬜ |
| [danmar/cppcheck](https://github.com/ZhangZhuoSJTU/cppcheck) | `0a5b103` | 2550 | 2124 | — | ⬜ |
| [direnv/direnv](https://github.com/ZhangZhuoSJTU/direnv) | `02040c7` | 986 | 847 | — | ⬜ |
| [doxygen/doxygen](https://github.com/ZhangZhuoSJTU/doxygen) | `966d98e` | 252 | 229 | — | ⬜ |
| [Drew-Alleman/DataSurgeon](https://github.com/ZhangZhuoSJTU/DataSurgeon) | `d257cee` | 564 | 498 | — | ⬜ |
| [ducaale/xh](https://github.com/ZhangZhuoSJTU/xh) | `4a6e44f` | 1266 | 1170 | — | ⬜ |
| [duckdb/duckdb](https://github.com/ZhangZhuoSJTU/duckdb) | `bdb65ec` | 8958 | 5,635 | — | ⬜ |
| [dundee/gdu](https://github.com/ZhangZhuoSJTU/gdu) | `ede21d2` | 1553 | 1121 | — | ⬜ |
| [ecumene/rust-sloth](https://github.com/ZhangZhuoSJTU/rust-sloth) | `051c559` | 455 | 377 | — | ⬜ |
| [ekzhang/bore](https://github.com/ZhangZhuoSJTU/bore) | `8e059cd` | 452 | 380 | — | ⬜ |
| [eliukblau/pixterm](https://github.com/ZhangZhuoSJTU/pixterm) | `1a93fd5` | 458 | 423 | — | ⬜ |
| [elkowar/pipr](https://github.com/ZhangZhuoSJTU/pipr) | `fae0b17` | 835 | 510 | — | ⬜ |
| [Epistates/treemd](https://github.com/ZhangZhuoSJTU/treemd) | `825c6dd` | 1961 | 1553 | — | ⬜ |
| [eradman/entr](https://github.com/ZhangZhuoSJTU/entr) | `8e2e8b4` | 685 | 569 | — | ⬜ |
| [Esubaalew/run](https://github.com/ZhangZhuoSJTU/run) | `0fb9dec` | 1507 | 1084 | — | ⬜ |
| [eudoxia0/hashcards](https://github.com/ZhangZhuoSJTU/hashcards) | `48aa136` | 1293 | 1018 | — | ⬜ |
| [facebook/zstd](https://github.com/ZhangZhuoSJTU/zstd) | `1168da0` | 2372 | 1975 | — | ⬜ |
| [facebookresearch/fastText](https://github.com/ZhangZhuoSJTU/fastText) | `1142dc4` | 352 | 301 | — | ⬜ |
| [FiloSottile/age](https://github.com/ZhangZhuoSJTU/age) | `706dfc1` | 839 | 672 | — | ⬜ |
| [foriequal0/git-trim](https://github.com/ZhangZhuoSJTU/git-trim) | `07c2f50` | 726 | 498 | — | ⬜ |
| [gabotechs/dep-tree](https://github.com/ZhangZhuoSJTU/dep-tree) | `60a95a2` | 1428 | 827 | — | ⬜ |
| [ggreer/the_silver_searcher](https://github.com/ZhangZhuoSJTU/the_silver_searcher) | `a61f178` | 1192 | 960 | — | ⬜ |
| [git-bahn/git-graph](https://github.com/ZhangZhuoSJTU/git-graph) | `87b4473` | 733 | 560 | — | ⬜ |
| [go-critic/go-critic](https://github.com/ZhangZhuoSJTU/go-critic) | `9aea378` | 925 | 493 | — | ⬜ |
| [google/brotli](https://github.com/ZhangZhuoSJTU/brotli) | `b3dc9cc` | 606 | 441 | — | ⬜ |
| [gromacs/gromacs](https://github.com/ZhangZhuoSJTU/gromacs) | `665ea4c` | 1382 | 1,168 | — | ⬜ |
| [guumaster/hostctl](https://github.com/ZhangZhuoSJTU/hostctl) | `d6d9699` | 1385 | 1051 | — | ⬜ |
| [hairyhenderson/gomplate](https://github.com/ZhangZhuoSJTU/gomplate) | `05eb3aa` | 3538 | 2905 | — | ⬜ |
| [HaliteChallenge/Halite](https://github.com/ZhangZhuoSJTU/Halite) | `822cfb6` | 391 | 275 | — | ⬜ |
| [hatoo/oha](https://github.com/ZhangZhuoSJTU/oha) | `8dc6349` | 1095 | 887 | — | ⬜ |
| [hooklift/gowsdl](https://github.com/ZhangZhuoSJTU/gowsdl) | `2a06cec` | 419 | 391 | — | ⬜ |
| [hpjansson/chafa](https://github.com/ZhangZhuoSJTU/chafa) | `dd4d4c1` | 2775 | 1605 | — | ⬜ |
| [htop-dev/htop](https://github.com/ZhangZhuoSJTU/htop) | `523600b` | 1200 | 616 | — | ⬜ |
| [hush-shell/hush](https://github.com/ZhangZhuoSJTU/hush) | `560c33a` | 1298 | 1198 | — | ⬜ |
| [incu6us/goimports-reviser](https://github.com/ZhangZhuoSJTU/goimports-reviser) | `81bd549` | 597 | 512 | — | ⬜ |
| [ip7z/7zip](https://github.com/ZhangZhuoSJTU/7zip) | `839151e` | 1085 | 970 | — | ⬜ |
| [ismaelgv/rnr](https://github.com/ZhangZhuoSJTU/rnr) | `fc0733b` | 742 | 680 | — | ⬜ |
| [ivanceras/svgbob](https://github.com/ZhangZhuoSJTU/svgbob) | `6d00ad9` | 474 | 472 | — | ⬜ |
| [jhspetersson/fselect](https://github.com/ZhangZhuoSJTU/fselect) | `c3559ca` | 3435 | 2855 | — | ⬜ |
| [JohannesKaufmann/html-to-markdown](https://github.com/ZhangZhuoSJTU/html-to-markdown) | `3006818` | 974 | 884 | — | ⬜ |
| [johnkerl/miller](https://github.com/ZhangZhuoSJTU/miller) | `8d85b46` | 16070 | 14543 | — | ⬜ |
| [jqlang/jq](https://github.com/ZhangZhuoSJTU/jq) | `b33a763` | 6796 | 6032 | — | ⬜ |
| [jrnxf/thokr](https://github.com/ZhangZhuoSJTU/thokr) | `09375ef` | 507 | 378 | — | ⬜ |
| [junegunn/fzf](https://github.com/ZhangZhuoSJTU/fzf) | `b56d614` | 2164 | 1846 | — | ⬜ |
| [kaushiksrini/parqeye](https://github.com/ZhangZhuoSJTU/parqeye) | `8072121` | 564 | 346 | — | ⬜ |
| [kisielk/errcheck](https://github.com/ZhangZhuoSJTU/errcheck) | `dacab89` | 532 | 340 | — | ⬜ |
| [konradsz/igrep](https://github.com/ZhangZhuoSJTU/igrep) | `aa75630` | 728 | 343 | — | ⬜ |
| [kyoh86/richgo](https://github.com/ZhangZhuoSJTU/richgo) | `313114f` | 787 | 531 | — | ⬜ |
| [kyoheiu/felix](https://github.com/ZhangZhuoSJTU/felix) | `95df390` | 979 | 379 | — | ⬜ |
| [lfos/calcurse](https://github.com/ZhangZhuoSJTU/calcurse) | `49180d5` | 1994 | 555 | — | ⬜ |
| [lh3/seqtk](https://github.com/ZhangZhuoSJTU/seqtk) | `94e7070` | 440 | 428 | — | ⬜ |
| [lua/lua](https://github.com/ZhangZhuoSJTU/lua) | `c6b4848` | 1387 | 1328 | — | ⬜ |
| [LuaJIT/LuaJIT](https://github.com/ZhangZhuoSJTU/LuaJIT) | `a553b3d` | 3183 | 2931 | — | ⬜ |
| [Lymphatus/caesium-clt](https://github.com/ZhangZhuoSJTU/caesium-clt) | `a529b2e` | 616 | 575 | — | ⬜ |
| [lz4/lz4](https://github.com/ZhangZhuoSJTU/lz4) | `1519f46` | 1829 | 1484 | — | ⬜ |
| [madler/pigz](https://github.com/ZhangZhuoSJTU/pigz) | `fe4894f` | 938 | 829 | — | ⬜ |
| [mfridman/tparse](https://github.com/ZhangZhuoSJTU/tparse) | `2416b4b` | 556 | 417 | — | ⬜ |
| [mgdm/htmlq](https://github.com/ZhangZhuoSJTU/htmlq) | `6e31bc8` | 2058 | 1455 | — | ⬜ |
| [mgechev/revive](https://github.com/ZhangZhuoSJTU/revive) | `201451e` | 886 | 727 | — | ⬜ |
| [mibk/dupl](https://github.com/ZhangZhuoSJTU/dupl) | `1bf052b` | 450 | 370 | — | ⬜ |
| [mikefarah/yq](https://github.com/ZhangZhuoSJTU/yq) | `602586d` | 2046 | 1996 | — | ⬜ |
| [Miserlou/Loop](https://github.com/ZhangZhuoSJTU/Loop) | `209927c` | 778 | 709 | — | ⬜ |
| [mookid/diffr](https://github.com/ZhangZhuoSJTU/diffr) | `2152742` | 782 | 606 | — | ⬜ |
| [multiprocessio/dsq](https://github.com/ZhangZhuoSJTU/dsq) | `c3ae0ba` | 766 | 542 | — | ⬜ |
| [nachoparker/dutree](https://github.com/ZhangZhuoSJTU/dutree) | `44e877d` | 957 | 499 | — | ⬜ |
| [naggie/dstask](https://github.com/ZhangZhuoSJTU/dstask/tree/main) | `ff57396` | 1589 | 1276 | — | ⬜ |
| [nikolassv/bartib](https://github.com/ZhangZhuoSJTU/bartib) | `6b9b5ce` | 929 | 720 | — | ⬜ |
| [ninja-build/ninja](https://github.com/ZhangZhuoSJTU/ninja) | `cc60300` | 1905 | 1422 | — | ⬜ |
| [noborus/trdsql](https://github.com/ZhangZhuoSJTU/trdsql) | `d8c5ff6` | 1403 | 1308 | — | ⬜ |
| [Nukesor/pueue](https://github.com/ZhangZhuoSJTU/pueue) | `8b9d6fe` | 1223 | 634 | — | ⬜ |
| [o2sh/onefetch](https://github.com/ZhangZhuoSJTU/onefetch) | `e5958ce` | 1214 | 1114 | — | ⬜ |
| [ogham/dog](https://github.com/ZhangZhuoSJTU/dog) | `721440b` | 1722 | 964 | — | ⬜ |
| [oppiliappan/eva](https://github.com/ZhangZhuoSJTU/eva) | `41ae245` | 963 | 913 | — | ⬜ |
| [oppiliappan/statix](https://github.com/ZhangZhuoSJTU/statix) | `e9df54c` | 983 | 813 | — | ⬜ |
| [orf/gping](https://github.com/ZhangZhuoSJTU/gping) | `26eb5b9` | 655 | 289 | — | ⬜ |
| [paradigmxyz/solar](https://github.com/ZhangZhuoSJTU/solar) | `5190d0e` | 2528 | 1,973 | — | ⬜ |
| [parcel-bundler/lightningcss](https://github.com/ZhangZhuoSJTU/lightningcss) | `aa2ed1e` | 3155 | 2,828 | — | ⬜ |
| [peco/peco](https://github.com/ZhangZhuoSJTU/peco) | `4e58dad` | 1715 | 1187 | — | ⬜ |
| [pemistahl/grex](https://github.com/ZhangZhuoSJTU/grex) | `fa3e8ed` | 1518 | 1311 | — | ⬜ |
| [php/php-src](https://github.com/ZhangZhuoSJTU/php-src) | `c891263` | 20530 | 14,269 | — | ⬜ |
| [pier-cli/pier](https://github.com/ZhangZhuoSJTU/pier) | `5e1bde9` | 779 | 680 | — | ⬜ |
| [pls-rs/pls](https://github.com/ZhangZhuoSJTU/pls) | `4e1ae50` | 354 | 297 | — | ⬜ |
| [psampaz/go-mod-outdated](https://github.com/ZhangZhuoSJTU/go-mod-outdated) | `bb79367` | 342 | 284 | — | ⬜ |
| [quinn-rs/quinn](https://github.com/ZhangZhuoSJTU/quinn) | `bb359cc` | 620 | 492 | — | ⬜ |
| [raviqqe/muffet](https://github.com/ZhangZhuoSJTU/muffet) | `a882908` | 432 | 292 | — | ⬜ |
| [rcoh/angle-grinder](https://github.com/ZhangZhuoSJTU/angle-grinder) | `9c2fc88` | 1143 | 1126 | — | ⬜ |
| [rhysd/kiro-editor](https://github.com/ZhangZhuoSJTU/kiro-editor) | `4157485` | 770 | 519 | — | ⬜ |
| [riquito/tuc](https://github.com/ZhangZhuoSJTU/tuc) | `16fb471` | 1249 | 1195 | — | ⬜ |
| [robertdavidgraham/masscan](https://github.com/ZhangZhuoSJTU/masscan) | `b99d433` | 3357 | 1490 | — | ⬜ |
| [rochacbruno/marmite](https://github.com/ZhangZhuoSJTU/marmite) | `7d4bc2d` | 853 | 668 | — | ⬜ |
| [rs/curlie](https://github.com/ZhangZhuoSJTU/curlie) | `5dfcbb1` | 741 | 681 | — | ⬜ |
| [rs/jplot](https://github.com/ZhangZhuoSJTU/jplot) | `2a54bcc` | 722 | 438 | — | ⬜ |
| [rust-embedded/svd2rust](https://github.com/ZhangZhuoSJTU/svd2rust) | `1760b5e` | 985 | 918 | — | ⬜ |
| [rust-ethereum/ethabi](https://github.com/ZhangZhuoSJTU/ethabi) | `b1710ad` | 1053 | 997 | — | ⬜ |
| [rust-lang/mdBook](https://github.com/ZhangZhuoSJTU/mdBook) | `37273ba` | 1326 | 1098 | — | ⬜ |
| [rvben/rumdl](https://github.com/ZhangZhuoSJTU/rumdl) | `2d75c4d` | 4781 | 3256 | — | ⬜ |
| [samtools/samtools](https://github.com/ZhangZhuoSJTU/samtools) | `aa823b5` | 1819 | 1,386 | — | ⬜ |
| [sayanarijit/xplr](https://github.com/ZhangZhuoSJTU/xplr) | `1751065` | 939 | 305 | — | ⬜ |
| [sclevine/yj](https://github.com/ZhangZhuoSJTU/yj) | `8016400` | 825 | 768 | — | ⬜ |
| [segmentio/chamber](https://github.com/ZhangZhuoSJTU/chamber) | `5f93f5f` | 3104 | 1526 | — | ⬜ |
| [sharkdp/bat](https://github.com/ZhangZhuoSJTU/bat-sharkdp) | `f822bd0` | 986 | 796 | — | ⬜ |
| [sharkdp/fd](https://github.com/ZhangZhuoSJTU/fd) | `40d8eb3` | 1405 | 1190 | — | ⬜ |
| [sharkdp/hexyl](https://github.com/ZhangZhuoSJTU/hexyl) | `2e26437` | 974 | 906 | — | ⬜ |
| [sharkdp/hyperfine](https://github.com/ZhangZhuoSJTU/hyperfine) | `327d5f4` | 298 | 290 | — | ⬜ |
| [sharkdp/pastel](https://github.com/ZhangZhuoSJTU/pastel) | `b60e899` | 1256 | 1103 | — | ⬜ |
| [sibprogrammer/xq](https://github.com/ZhangZhuoSJTU/xq) | `b89f681` | 879 | 791 | — | ⬜ |
| [sigoden/argc](https://github.com/ZhangZhuoSJTU/argc) | `04a08f1` | 1410 | 975 | — | ⬜ |
| [simeg/eureka](https://github.com/ZhangZhuoSJTU/eureka) | `df3796c` | 400 | 343 | — | ⬜ |
| [sirwart/ripsecrets](https://github.com/ZhangZhuoSJTU/ripsecrets) | `34c9e03` | 937 | 611 | — | ⬜ |
| [sitkevij/hex](https://github.com/ZhangZhuoSJTU/hex) | `61ae69b` | 877 | 822 | — | ⬜ |
| [sqlite/sqlite](https://github.com/ZhangZhuoSJTU/sqlite) | `839433d` | 16801 | 13,491 | — | ⬜ |
| [sstadick/hck](https://github.com/ZhangZhuoSJTU/hck) | `b66c751` | 884 | 854 | — | ⬜ |
| [stacked-git/stgit](https://github.com/ZhangZhuoSJTU/stgit) | `430027d` | 2340 | 1,469 | — | ⬜ |
| [Stranger6667/jsonschema](https://github.com/ZhangZhuoSJTU/jsonschema) | `d52e881` | 3006 | 2,931 | — | ⬜ |
| [svenstaro/genact](https://github.com/ZhangZhuoSJTU/genact) | `16f96e3` | 237 | 221 | — | ⬜ |
| [svenstaro/miniserve](https://github.com/ZhangZhuoSJTU/miniserve) | `8449e8b` | 440 | 301 | — | ⬜ |
| [tarka/xcp](https://github.com/ZhangZhuoSJTU/xcp) | `5e5b448` | 1236 | 1,091 | — | ⬜ |
| [TheZoraiz/ascii-image-converter](https://github.com/ZhangZhuoSJTU/ascii-image-converter) | `d05a757` | 488 | 451 | — | ⬜ |
| [tomarrell/wrapcheck](https://github.com/ZhangZhuoSJTU/wrapcheck) | `c058da1` | 669 | 477 | — | ⬜ |
| [tomnomnom/gron](https://github.com/ZhangZhuoSJTU/gron) | `88a6234` | 233 | 220 | — | ⬜ |
| [tree-sitter/tree-sitter](https://github.com/ZhangZhuoSJTU/tree-sitter) | `5e23cca` | 1888 | 1,145 | — | ⬜ |
| [tukaani-project/xz](https://github.com/ZhangZhuoSJTU/xz) | `1007bf0` | 2036 | 1,392 | — | ⬜ |
| [typst/typst](https://github.com/ZhangZhuoSJTU/typst) | `88356d0` | 1789 | 1,711 | — | ⬜ |
| [unhappychoice/gittype](https://github.com/ZhangZhuoSJTU/gittype) | `34b72d0` | 932 | 576 | — | ⬜ |
| [universal-ctags/ctags](https://github.com/ZhangZhuoSJTU/ctags) | `243595e` | 2579 | 2,248 | — | ⬜ |
| [wfxr/code-minimap](https://github.com/ZhangZhuoSJTU/code-minimap) | `0ddeea5` | 370 | 312 | — | ⬜ |
| [wfxr/csview](https://github.com/ZhangZhuoSJTU/csview) | `8ac4de0` | 348 | 334 | — | ⬜ |
| [WGUNDERWOOD/tex-fmt](https://github.com/ZhangZhuoSJTU/tex-fmt) | `3f1aef6` | 495 | 455 | — | ⬜ |
| [wintermute-cell/ngrrram](https://github.com/ZhangZhuoSJTU/ngrrram) | `8ea13c3` | 332 | 300 | — | ⬜ |
| [XAMPPRocky/tokei](https://github.com/ZhangZhuoSJTU/tokei) | `505d648` | 760 | 731 | — | ⬜ |
| [Y2Z/monolith](https://github.com/ZhangZhuoSJTU/monolith) | `8702e66` | 777 | 712 | — | ⬜ |
| [yaa110/nomino](https://github.com/ZhangZhuoSJTU/nomino) | `f892499` | 338 | 307 | — | ⬜ |
| [yassinebridi/serpl](https://github.com/ZhangZhuoSJTU/serpl) | `c48a9d7` | 536 | 404 | — | ⬜ |
| [yoav-lavi/melody](https://github.com/ZhangZhuoSJTU/melody) | `f4af9b4` | 1438 | 1194 | — | ⬜ |
| [zevv/duc](https://github.com/ZhangZhuoSJTU/duc) | `a58fa4e` | 1246 | 817 | — | ⬜ |
| [zk-org/zk](https://github.com/ZhangZhuoSJTU/zk) | `10d93d5` | 1473 | 1060 | — | ⬜ |
