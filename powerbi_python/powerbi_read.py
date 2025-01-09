import nbformat
from nbclient import NotebookClient


def execute_notebook_like_click(input_path, output_path, parameters=None):
    """
    Execute a Jupyter notebook cell by cell, simulating the "execute cell" button.

    Args:
        input_path (str): Path to the input notebook.
        output_path (str): Path to save the executed notebook.
        parameters (dict, optional): Parameters to inject into the notebook.
    """
    try:
        print("Starting notebook execution cell by cell (simulating execute button)...")

        # Load the notebook
        with open(input_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Inject parameters into the first cell if provided
        if parameters:
            param_cell = nbformat.v4.new_code_cell(source=f"# Injected parameters\n{parameters}")
            notebook['cells'].insert(0, param_cell)

        # Create a NotebookClient instance
        client = NotebookClient(notebook, kernel_name="python3", timeout=600)

        # Start the client to execute the notebook
        client.execute()

        # Save the executed notebook
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)

        print(f"Notebook executed successfully and saved to {output_path}")

    except Exception as e:
        print(f"Error during notebook execution: {e}")


if __name__ == "__main__":
    # Replace these with your notebook paths
    input_notebook = "powerbi_rag.ipynb"
    output_notebook = "executed_notebook1.ipynb"

    execute_notebook_like_click(input_notebook, output_notebook)
