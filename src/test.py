import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    dut.wrEn.value = 0
    
    dut._log.info("reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 10)
    dut.rst.value = 0
    await ClockCycles(dut.clk, 10)

    await RisingEdge(dut.clk)
    dut.wrEn.value = 1
    dut.data_in.value = 1
    await RisingEdge(dut.clk)
    dut.data_in.value = 0
    await RisingEdge(dut.clk)
    dut.data_in.value = 1
    await RisingEdge(dut.clk)
    dut.data_in.value = 0
    await RisingEdge(dut.clk)
    dut.wrEn.value = 0

    await Timer(100, 'us')