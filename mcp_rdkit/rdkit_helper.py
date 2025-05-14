# basic import 
from mcp.server.fastmcp import FastMCP  
import mcp.types as types
from rdkit import Chem
from rdkit.Chem import Draw
import base64
from rdkit.Chem import Descriptors
import pandas
import requests
import io
from rdkit.Chem import AllChem

# instantiate an MCP server client
mcp = FastMCP("rdkit-mcp-server")

# DEFINE TOOLS
def pil_image_to_base64(img, format="PNG"):
    """
    Converts a PIL Image object to a base64 string.

    Args:
        img: PIL Image object.
        format: Image format for saving to buffer (e.g., "PNG", "JPEG").

    Returns:
        A base64 encoded string representation of the image.
    """
    buffered = io.BytesIO()
    img.save(buffered, format=format)
    img_byte = buffered.getvalue()
    img_str = base64.b64encode(img_byte).decode()
    return img_str

def img_byte_to_base64(img_byte):
    """
    Converts a byte array to a base64 string.

    Args:
        img_byte: Byte array of the image.

    Returns:
        A base64 encoded string representation of the image.
    """
    img_str = base64.b64encode(img_byte).decode()
    return img_str

@mcp.tool()
def smiles_to_image(smiles:str) :
    """Generate image from SMILES string"""
    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)
    print(dir(img))
    img_str = pil_image_to_base64(img)
    return types.ImageContent(
                    type="image", data=img_str, mimeType="image/png"
                )
            
@mcp.tool()
def get_molecule_descriptors_from_smiles(smiles:str):
    
    m = Chem.MolFromSmiles(smiles)
    descriptors = [Descriptors.CalcMolDescriptors(m)]
    df = pandas.DataFrame(descriptors)
    print(df.head())
    table_as_string = df.to_string(index=False)
    return table_as_string

@mcp.tool()
def visualize_chemical_reaction(smart_str:str):
    """Generate image for chemical reaction from SMARTS string"""
    
    rxn = AllChem.ReactionFromSmarts(smart_str,useSmiles=True)
    d2d = Draw.MolDraw2DCairo(800,300)
    d2d.DrawReaction(rxn)
    png = d2d.GetDrawingText()
    img_str = img_byte_to_base64(png)
    return types.ImageContent(
                    type="image", data=img_str, mimeType="image/png"
                )
    

@mcp.tool()
def search_substructure(smiles:str, substructure_smiles:str,use_chirality:bool=False):
    """Search for substructure in a molecule"""
    m = Chem.MolFromSmiles(smiles)
    substructure = Chem.MolFromSmiles(substructure_smiles)
    match = m.HasSubstructMatch(substructure,useChirality=use_chirality)
    print("MATCH",match)
    is_match = None
    if match:
        is_match = True
        matches = m.GetSubstructMatches(substructure)
        return types.TextContent(
            type="text",
                    text=f"Substructure found at: str {matches}",
                )

    else:
        is_match = False
        return types.TextContent(
            type="text",
                    text=f"Substructure not found",
        )

@mcp.tool()
def get_smiles_from_name(chemical_name:str):
    """Get SMILES string from name"""
    get_smile_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemical_name}/property/CanonicalSMILES/JSON"
    response = requests.get(get_smile_url)
    response_json = response.json()
    canonical_smiles = response_json["PropertyTable"]["Properties"][0].get("CanonicalSMILES","Sorry No SMILES found")
    return types.TextContent(
        type="text",
                text=f"SMILES: {canonical_smiles}",
            )

