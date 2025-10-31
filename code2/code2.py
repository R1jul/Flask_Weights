
from flask import Flask , request, jsonify
code2=Flask(__name__)

def kg_lb(kg : float):
    return kg * 2.20462

def lb_kg (lb : float):
    return lb / 2.20462

def convert():
    try:
        value=float(request.args.get("value",0))
        unit=request.args.get("unit","").lower()
        
        if unit == "kg":
            result=kg_lb(value)
        

        elif unit=="lb":
            result=lb_kg(value)
            message=f"{value}lb={result:.2f}kg"
            
        else:
            return jsonify({"error" : "Unit must be kg or lb"}),400
        
        
        return jsonify ({"Result vslur " : message})
    
    except Exception as e:
        return jsonify ({"error" : str(e)}),400
    
code2.add_url_rule("/convert",view_func=convert,methods=["GET"])

if __name__ == "__main__":
    code2.run(debug=True)
            
  