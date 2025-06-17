// testbench.sv

module testbench;
    logic clk = 0;
    logic rst;
    logic [1:0] init_state;
    logic [1:0] result;

    // Clock generation
    always #5 clk = ~clk;

    NeutralTrinaryUnit uut (
        .clk(clk),
        .rst(rst),
        .initial_state(init_state),
        .resolved_state(result)
    );

    initial begin
        $display("Starting simulation...");
        rst = 1;
        init_state = 2'b10; // '+/-' ambiguous state
        #10;
        rst = 0;

        // Run for a few cycles to observe resolution
        repeat (10) begin
            #10;
            $display("Resolved State = %b", result);
        end

        $finish;
    end
endmodule
