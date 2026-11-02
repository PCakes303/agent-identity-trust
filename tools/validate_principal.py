import json,sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
def validate(d):
 e=[]
 if not isinstance(d,dict): return ["principal must be an object"]
 for k in ("principal_id","principal_type","issuer","created_at"):
  if not isinstance(d.get(k),str) or not d[k].strip(): e.append(k+" must be non-empty")
 if d.get("principal_type") not in {"human","agent","service","workload"}: e.append("unsupported principal_type")
 u=d.get("issuer")
 if isinstance(u,str):
  p=urlparse(u)
  if p.scheme not in {"https","spiffe"} or not p.netloc: e.append("issuer must be an absolute HTTPS or SPIFFE URI")
 t=d.get("created_at")
 if isinstance(t,str):
  try: datetime.fromisoformat(t.replace("Z","+00:00"))
  except ValueError: e.append("created_at must be ISO 8601")
 if d.get("status","active") not in {"active","suspended","revoked","expired"}: e.append("unsupported status")
 return e
if __name__=="__main__":
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("examples/principal.json")
 try: d=json.loads(p.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as x: print(x,file=sys.stderr); sys.exit(2)
 e=validate(d)
 if e: print("\n".join(e),file=sys.stderr); sys.exit(1)
 print("valid principal record (not an authentication assertion)")
