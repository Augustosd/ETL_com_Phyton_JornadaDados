from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class Campanha(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês no formato 'AAAA | Mês'")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Tipo de dia")
    Objetivo: str = Field(..., description="Objetivo da campanha")
    Date: date = Field(..., description="Data no formato AAAA-MM-DD")
    AdSet_name: str = Field(..., description="Nome do AdSet")
    Amount_spent: float = Field(..., ge=0, le=2200, description="Valor gasto entre 0 e 2200")
    Link_clicks: Optional[int] = Field(None, description="Quantidade de cliques no link (valor ausente se não informado)")
    Impressions: int = Field(..., description="Número de impressões")
    Conversions: Optional[int] = Field(None, description="Quantidade de conversões (valor ausente se não informado)")
    Segmentacao: str = Field(..., alias="Segmentação", description="Segmentação da campanha")
    Tipo_de_Anuncio: str = Field(..., alias="Tipo_de_Anúncio", description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase da campanha")



    