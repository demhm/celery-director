from director.extensions import db
from director.models import BaseModel, StatusType
from director.models.utils import JSONBType


class Workflow(BaseModel):
    __tablename__ = "workflows"

    name = db.Column(db.String(255), nullable=False)
    project = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(StatusType), default=StatusType.pending, nullable=False)
    payload = db.Column(JSONBType, default={})
    periodic = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(255))
    created_by = db.Column(db.String(255))

    def __str__(self):
        return f"{self.project}.{self.name}"

    def __repr__(self):
        return f"<Workflow {self.project}.{self.name}>"

    def to_dict(self, with_payload=True):
        d = super().to_dict()
        d.update(
            {
                "name": self.name,
                "project": self.project,
                "fullname": f"{self.project}.{self.name}",
                "status": self.status.value,
                "periodic": self.periodic,
            }
        )
        if self.description is not None:
            d["description"] = self.description
        if self.created_by is not None:
            d["created_by"] = self.created_by
        if with_payload:
            d["payload"] = self.payload
        return d
