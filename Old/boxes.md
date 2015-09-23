ADK Mästarprov
==============

> Indata n antal lådor:
> Pseudokoden är mycket influerad av ADA.


```
type Box is record
  Height: Integer
  Width: Integer
  Length: Integer
end record;

procedure BoxInBoxes(Boxes: in Box[], res: out Integer)
  q := new Queue() // Priority queue, sorted in ascending order based on the volume.
  current_volume := Integer.min
  begin
    // Cost:= O(n log(n))
    for box in boxes:
      v := box.height * box.width * box.length //O(1)
      q.push((v,box)) //(log(n))
    end
    for b in q.poll() loop // O(n) for each iteration, get the top and delete the top
      if b.first > current_volume then
        current_volume = b.first
      end if
    end loop
  end BoxInBoxes
```
