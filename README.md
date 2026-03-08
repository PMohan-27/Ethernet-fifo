!![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# UWASIC W26: MAC learning table

## Getting Started

1. Clone this repository
2. Update [info.yaml](info.yaml) with your project details
3. Make a post in the [UWASIC Discord server](https://discord.gg/ZcfXmCkV) under **#onboarding/posts** to kick things off!
4. [Read the full documentation and specifications here](https://docs.uwasic.com/doc/fifo-buffer-N7lQ4OOpWb)

## Disclaimer

The final implementation will be integrated into an FPGA fabric of a larger SoC. This TinyTapeout template serves as a trackable starting point for initial prototyping and team training purposes.

## Set up your Verilog project

1. Add your Verilog files to the `src` folder.
2. Edit the [info.yaml](info.yaml) and update information about your project, paying special attention to the `source_files` and `top_module` properties. 
3. Edit [docs/info.md](docs/info.md) weekly and document your weekly progress on RTL and Verification, along with any comments or concerns you may have.

The GitHub action will automatically build the ASIC files using [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/).

## Writing cocotb Testbenches

This project has a hierarchical design structure:
- **`buffer_top`** (top module): Configurable Ethernet FIFO buffer with selectable sync/async modes - *not being tested in Phase 1*
  - **`fifo_sync`** (Phase 1 DUT): Synchronous FIFO implementation - *current verification target*
    - **`fifo_memory`** (submodule): Memory storage for FIFO data
    - **`counter`** (submodule): Increments with each successful read transaction to provide verification metrics

**For Phase 1, the testbench instantiates `fifo_sync` as the DUT.** This allows thorough verification of the synchronous FIFO functionality before integrating it into the configurable `buffer_top` module. The counter submodule provides an additional source of verification by tracking the number of successful read transactions. The test files you write and add uin `test/test.py` must contain test cases that can verify:
- FIFO write and read operations
- Empty and full flag behavior
- Data integrity and ordering
- Read transaction counter increments
- All behaviours under reset

In Phase 2, `fifo_sync` will be integrated into `buffer_top` along with `fifo_async` support and I/O interface testing.

> **Note:** If you're more comfortable using Verilog or SystemVerilog testbenches for verification, feel free to use those instead of cocotb.

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [Documentation](https://docs.uwasic.com/doc/fifo-buffer-N7lQ4OOpWb)

- [Synchronous Fifo design and verification](https://youtu.be/k13iGkDYStk?si=eXs8CoIwD8Yzng5z)

- [Synchronous Fifo: EDA Playground](https://www.edaplayground.com/x/p5Dd)


- [UWASIC discord server](https://discord.gg/ZcfXmCkV)
