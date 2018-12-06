describe("", function() {
  it("Declarada la variable diaDeSemana", function() {
    assert.notEqual(diaDeSemana, "undefined");
  });
    it("Le asigna el valor \"domingo\" a  diaDeSemana", function() {
    assert.equal(diaDeSemana, "domingo");
  });
    it("debería imprimir ''Hoy se juega al futbol!!!''", function() {
    assert.equal(console.toString(), "Hoy se juega al futbol!!!");
  });
})
