# Rozwizanie zadania rekrutacyjnego
Select [Table A].dimension_1,
       [Table MAP].correct_dimension_2 AS dimension_2,
       ISNULL(([Table A].measure_1),'0') AS measure_1,
       ISNULL(([Table B].measure_2),'0') AS measure_2
From [Table A] Inner Join [Table B] ON A.dimnsion_1 = B.dimension_1
               Inner Join [Table MAP] ON B.dimension_1 = MAP.dimension_1
