program ExempluStructuriControl;

type
            Zi = (Lun, Mar, Mie, Joi, Vin, Sam, Dum);

    var
Azi: Zi;
           Contor: Integer;

                 function EsteWeekend(Ziua: Zi): Boolean;
begin
          case Ziua of
    Sam, Dum: EsteWeekend := True;
 else EsteWeekend := False;
                                              end;
 end;

       procedure AfiseazaZi(Ziua: Zi);
 begin
if EsteWeekend(Ziua) then
WriteLn('Este weekend.')
else
begin
  WriteLn('Este o zi lucrătoare.');
                   end;
end;


        begin
Azi := Lun;
         Contor := 0;

  repeat
 WriteLn('Zi ', Contor + 1);
            AfiseazaZi(Azi);
    Azi := Succ(Azi);
         Contor := Contor + 1;
until Azi = Dum;

                         WriteLn('Rezumatul săptămânii:');
for Azi := Lun to Dum do
        begin

  Write('Zi: ');
    case Azi of
                   Lun: WriteLn('Luni')   ;  { exemplu de comentariu }
      Mar: WriteLn('Marți');
                                      Mie: WriteLn('Miercuri');
  Joi: WriteLn('Joi');
          Vin: WriteLn('Vineri');
                  Sam: WriteLn('Sâmbătă');
  Dum: WriteLn('Duminică')       ;
                            end;
  end;

      while Contor > 0              do
  begin
 WriteLn('Numărătoare inversă: ', Contor);
            Contor := Contor - 1;
  end         ;

end.
