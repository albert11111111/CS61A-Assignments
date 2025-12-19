# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **CS61A Project 1: Hog** - a Python-based dice game implementation for UC Berkeley's CS61A course. Students implement game mechanics and AI strategies while learning fundamental programming concepts.

## Common Development Commands

### Testing
```bash
# Run all tests
python3 ok

# Test specific problem (00-12)
python3 ok -q 00
python3 ok -q 12

# Verbose output (show all tests)
python3 ok -v

# Interactive debugging after failed test
python3 ok -q 00 -i

# Run tests without network access
python3 ok --local
```

### Running Experiments
```bash
# Run strategy experiments and performance analysis
python3 hog.py --run_experiments
```

### Web GUI
```bash
# Start web server for visual game interface (port 31415)
python3 hog_gui.py
```

## Architecture & Structure

### Core Game Implementation (`hog.py`)
The project is organized into two main phases:

**Phase 1: Simulator (Problems 1-5)**
- `roll_dice()`: Dice rolling mechanics with pig-out rule
- `boar_brawl()`: Special scoring rule for rolling 0 dice
- `take_turn()`: Execute a single turn
- `simple_update()` / `sus_update()`: Score update functions with/without Sus Fuss rule
- `play()`: Main game loop simulation

**Phase 2: Strategies (Problems 6-12)**
- `always_roll()`: Basic strategy factory
- `make_averaged()`: Statistical analysis utility
- `boar_strategy()`: Boar Brawl optimization strategy
- `sus_strategy()`: Sus Fuss optimization strategy
- `final_strategy()`: Student's optimized strategy

### Supporting Modules
- `dice.py`: Fair dice and test dice implementations
- `ucb.py`: Course utilities (decorators, tracing, debugging)
- `hog_gui.py`: Flask web server for GUI interaction
- `default_graphics.py`: SVG dice graphics

### Testing Framework
- Uses custom `ok` testing framework (standalone executable)
- 13 test files (`tests/00.py` through `tests/12.py`)
- Doctest-based with locked/unlocked test cases
- Strategy validation through `check_strategy.py`

## Key Implementation Details

### Game Rules
- **Goal**: First to reach 100 points wins
- **Pig Out**: Roll a 1 → lose all points for that turn
- **Boar Brawl**: Roll 0 dice → score based on opponent's score digits
- **Sus Fuss**: Prime number of factors → score becomes next prime

### Strategy Development
- Strategies are functions: `(player_score, opponent_score) → num_rolls`
- Use `average_win_rate()` to evaluate strategy performance
- `run_experiments()` provides baseline comparisons
- Focus on optimizing `final_strategy()` for maximum win rate

### Testing Approach
- Complete problems sequentially (00 → 12)
- Each problem builds on previous implementations
- Use `python3 ok -q XX -i` for interactive debugging
- Test strategies with `check_strategy.py` validation

## Development Tips

1. **Start with Phase 1**: Complete simulator functions before strategies
2. **Use test dice**: `make_test_dice()` for predictable testing
3. **Strategy optimization**: Focus on edge cases and opponent score analysis
4. **Performance matters**: Efficient strategies win more games
5. **Experiment freely**: Use `run_experiments()` to test strategy variations