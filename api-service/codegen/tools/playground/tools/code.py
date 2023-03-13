from langchain.agents import tool

from codegen.tools.playground.mock.request import MockRequestFactory
from codegen.tools.playground.playground import NodeJSPlayground
from codegen.tools.playground.tools.process import encode_command_output


def extract_code(code: str):
    return code.strip().strip("`").strip()


def create_code_tools(playground: NodeJSPlayground, mock: MockRequestFactory):
    # Ensure that the function is a generator even if no tools are yielded
    yield from ()

    @tool("InstallNPMDependencies")
    def install_dependencies(dependencies: str) -> str:
        """
        Install specified dependecies with NPM and return errors.
        The input should be a list of Node.js dependencies separated by spaces.
        """
        output = playground.install_dependencies(extract_code(dependencies))
        result = encode_command_output(output, only_errors=True)
        return result if len(result) > 0 else "All dependencies installed"

    yield install_dependencies

    @tool("RunTypeScriptCode")
    def run_typescript_code(code: str) -> str:
        """
        Run the specified TypeScript code and return errors and output.
        The input should be a valid TypeScript code.
        The returned result will be the output and errors returned when executing the code.
        """
        output = playground.run_typescript_code(extract_code(code))
        result = encode_command_output(output)

        return result if len(result) > 0 else "Code execution finished without error"

    # yield run_typescript_code

    @tool("CheckTypeScriptCodeTypes")
    def check_typescript_code_types(code: str) -> str:
        """
        Check TypeScript types in the specified code and return errors.
        """
        output = playground.check_typescript_code(extract_code(code))
        result = encode_command_output(output, only_errors=True)

        return result if len(result) > 0 else "Typechecking finished without error"

    # yield check_typescript_code_types

    # This tool is just for executing JavaScript without doing the request to server
    # @tool("RunJavaScriptCode")
    # def run_javascript_code(code: str) -> str:
    #     """
    #     Run JavaScript code and return errors and output.
    #     Input should be a valid JavaScript code.
    #     """
    #     output = playground.run_javascript_code(extract_code(code))
    #     result = encode_command_output(output)
    #     return result if len(result) > 0 else "Code execution finished without error"

    # yield run_javascript_code

    @tool("RunJavaScriptCode")
    def run_javascript_code(code: str) -> str:
        """
        Execute JavaScript code that should start a server then tests if server correctly handles needed requests.
        The input should be a valid JavaScriptCode.
        The server should run on http://localhost:3000.
        The returned result is a the testing request output followed by the server code output and errors.
        """

        mock_request_command = mock.terminal_command()

        port = 3000
        test_output, server_output = playground.test_javascript_server_code(
            code=code, test_cmd=mock_request_command, port=port
        )

        test_result = encode_command_output(test_output)
        server_result = encode_command_output(server_output)

        return f"Test request result:\n{test_result}\nCode execution result:\n{server_result}"

    yield run_javascript_code